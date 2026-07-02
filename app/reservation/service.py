import uuid

from app.database.db import get_connection
from app.utils.pii import mask_name, mask_email


def create_reservation(
    guest_name,
    email,
    check_in,
    check_out,
    room_type
):
    """
    Create a new reservation.
    """

    conn = get_connection()
    cursor = conn.cursor()

    reservation_id = "RES-" + str(uuid.uuid4())[:8].upper()

    cursor.execute(
        """
        INSERT INTO reservations
        (
            reservation_id,
            guest_name,
            email,
            check_in,
            check_out,
            room_type,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            reservation_id,
            guest_name,
            email,
            check_in,
            check_out,
            room_type,
            "ACTIVE"
        )
    )

    conn.commit()
    conn.close()

    return reservation_id


def view_reservation(reservation_id):
    """
    View reservation using Reservation ID.

    PII (Guest Name & Email) is masked before returning.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM reservations
        WHERE reservation_id = ?
        """,
        (reservation_id,)
    )

    reservation = cursor.fetchone()

    conn.close()

    if reservation is None:
        return None

    return (
        reservation[0],                    # Reservation ID
        mask_name(reservation[1]),         # Guest Name (Masked)
        mask_email(reservation[2]),        # Email (Masked)
        reservation[3],                    # Check-in
        reservation[4],                    # Check-out
        reservation[5],                    # Room Type
        reservation[6]                     # Status
    )


def cancel_reservation(reservation_id):
    """
    Cancel a reservation.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE reservations
        SET status = ?
        WHERE reservation_id = ?
        """,
        (
            "CANCELLED",
            reservation_id
        )
    )

    conn.commit()

    success = cursor.rowcount > 0

    conn.close()

    return success


if __name__ == "__main__":

    print("=" * 50)
    print("Creating Reservation")
    print("=" * 50)

    reservation_id = create_reservation(
        guest_name="Nivetha",
        email="nivetha@gmail.com",
        check_in="2026-07-10",
        check_out="2026-07-12",
        room_type="Deluxe"
    )

    print("Reservation Created Successfully!")
    print("Reservation ID:", reservation_id)

    print("\n" + "=" * 50)
    print("Viewing Reservation")
    print("=" * 50)

    reservation = view_reservation(reservation_id)

    print(reservation)

    print("\n" + "=" * 50)
    print("Cancelling Reservation")
    print("=" * 50)

    success = cancel_reservation(reservation_id)

    if success:
        print("Reservation Cancelled Successfully!")
    else:
        print("Reservation Not Found!")

    print("\n" + "=" * 50)
    print("Viewing Updated Reservation")
    print("=" * 50)

    reservation = view_reservation(reservation_id)

    print(reservation)