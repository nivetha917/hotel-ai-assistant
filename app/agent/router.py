from app.guardrails.guardrails import check_guardrails

from app.rag.rag_service import ask_question

from app.reservation.service import (
    create_reservation,
    view_reservation,
    cancel_reservation
)


class HotelAgent:

    def process(self, user_input: str):

        # -------------------------------------------------
        # Guardrails
        # -------------------------------------------------

        allowed, message = check_guardrails(user_input)

        if not allowed:
            return message

        text = user_input.lower()

        # -------------------------------------------------
        # Create Reservation
        # -------------------------------------------------

        if any(word in text for word in [
            "book",
            "reserve",
            "reservation"
        ]):

            print("\nEnter Reservation Details\n")

            guest_name = input("Guest Name : ")
            email = input("Email      : ")
            check_in = input("Check-in   : ")
            check_out = input("Check-out  : ")
            room_type = input("Room Type  : ")

            reservation_id = create_reservation(
                guest_name=guest_name,
                email=email,
                check_in=check_in,
                check_out=check_out,
                room_type=room_type
            )

            return (
                f"\nReservation Created Successfully!\n"
                f"Reservation ID : {reservation_id}"
            )

        # -------------------------------------------------
        # View Reservation
        # -------------------------------------------------

        elif "view" in text:

            reservation_id = input("Reservation ID : ")

            reservation = view_reservation(reservation_id)

            if reservation:

                return f"""
Reservation ID : {reservation[0]}
Guest Name     : {reservation[1]}
Email          : {reservation[2]}
Check-in       : {reservation[3]}
Check-out      : {reservation[4]}
Room Type      : {reservation[5]}
Status         : {reservation[6]}
"""

            return "Reservation not found."

        # -------------------------------------------------
        # Cancel Reservation
        # -------------------------------------------------

        elif "cancel" in text:

            reservation_id = input("Reservation ID : ")

            success = cancel_reservation(reservation_id)

            if success:
                return "Reservation Cancelled Successfully."

            return "Reservation not found."

        # -------------------------------------------------
        # Everything else goes to RAG
        # -------------------------------------------------

        return ask_question(user_input)


if __name__ == "__main__":

    agent = HotelAgent()

    print("=" * 60)
    print("🏨 Hotel Reservation Assistant")
    print("=" * 60)
    print("Type 'exit', 'quit', or 'bye' to end the conversation.")

    while True:

        question = input("\nYou : ")

        if question.lower() in ["exit", "quit", "bye"]:

            print("\nAssistant:")
            print("👋 Thank you for using the Hotel Reservation Assistant.")
            print("Have a great day!")

            break

        answer = agent.process(question)

        print("\nAssistant:\n")
        print(answer)