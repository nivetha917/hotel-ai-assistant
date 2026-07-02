import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import streamlit as st

from app.rag.rag_service import ask_question
from app.reservation.service import (
    create_reservation,
    view_reservation,
    cancel_reservation,
)

st.set_page_config(
    page_title="Hotel Reservation Assistant",
    page_icon="🏨",
    layout="wide"
)

st.title("🏨 Hotel Reservation Assistant")
st.write("Ask hotel questions or manage reservations.")

st.divider()

# ============================================================
# HOTEL QUESTIONS
# ============================================================

st.header("💬 Ask About the Hotel")

question = st.text_input("Enter your question")

if st.button("Ask"):

    if question.strip():

        answer = ask_question(question)

        st.success(answer)

    else:

        st.warning("Please enter a question.")

st.divider()

# ============================================================
# CREATE RESERVATION
# ============================================================

st.header("📅 Create Reservation")

guest_name = st.text_input("Guest Name")

email = st.text_input("Email")

check_in = st.date_input("Check-in Date")

check_out = st.date_input("Check-out Date")

room_type = st.selectbox(
    "Room Type",
    ["Standard", "Deluxe", "Suite"]
)

if st.button("Create Reservation"):

    reservation_id = create_reservation(
        guest_name=guest_name,
        email=email,
        check_in=str(check_in),
        check_out=str(check_out),
        room_type=room_type
    )

    st.success(f"Reservation Created Successfully!\n\nReservation ID: {reservation_id}")

st.divider()

# ============================================================
# VIEW RESERVATION
# ============================================================

st.header("🔍 View Reservation")

reservation_id = st.text_input("Reservation ID")

if st.button("View"):

    reservation = view_reservation(reservation_id)

    if reservation:

        st.write(f"Reservation ID : {reservation[0]}")
        st.write(f"Guest Name : {reservation[1]}")
        st.write(f"Email : {reservation[2]}")
        st.write(f"Check In : {reservation[3]}")
        st.write(f"Check Out : {reservation[4]}")
        st.write(f"Room Type : {reservation[5]}")
        st.write(f"Status : {reservation[6]}")

    else:

        st.error("Reservation not found.")

st.divider()

# ============================================================
# CANCEL RESERVATION
# ============================================================

st.header("❌ Cancel Reservation")

cancel_id = st.text_input("Reservation ID to Cancel")

if st.button("Cancel"):

    success = cancel_reservation(cancel_id)

    if success:

        st.success("Reservation Cancelled Successfully!")

    else:

        st.error("Reservation not found.")