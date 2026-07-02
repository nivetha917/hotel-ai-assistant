from langchain.tools import tool

from app.rag.rag_service import ask_question
from app.reservation.service import (
    create_reservation,
    view_reservation,
    cancel_reservation
)


@tool
def hotel_qa(question: str) -> str:
    """
    Answer hotel-related questions using the hotel document (RAG).
    Use this tool for questions about:
    - hotel facilities
    - check-in/check-out
    - food
    - hygiene
    - cancellation policy
    - dining
    - location
    """
    return ask_question(question)


@tool
def create_booking(
    guest_name: str,
    email: str,
    check_in: str,
    check_out: str,
    room_type: str
) -> str:
    """
    Create a new hotel reservation.
    """

    reservation_id = create_reservation(
        guest_name=guest_name,
        email=email,
        check_in=check_in,
        check_out=check_out,
        room_type=room_type
    )

    return f"Reservation created successfully.\nReservation ID: {reservation_id}"


@tool
def view_booking(reservation_id: str) -> str:
    """
    View reservation details using Reservation ID.
    """

    reservation = view_reservation(reservation_id)

    if reservation is None:
        return "Reservation not found."

    return (
        f"Reservation ID: {reservation[0]}\n"
        f"Guest Name: {reservation[1]}\n"
        f"Email: {reservation[2]}\n"
        f"Check-in: {reservation[3]}\n"
        f"Check-out: {reservation[4]}\n"
        f"Room Type: {reservation[5]}\n"
        f"Status: {reservation[6]}"
    )


@tool
def cancel_booking(reservation_id: str) -> str:
    """
    Cancel a reservation using Reservation ID.
    """

    success = cancel_reservation(reservation_id)

    if success:
        return "Reservation cancelled successfully."

    return "Reservation not found."