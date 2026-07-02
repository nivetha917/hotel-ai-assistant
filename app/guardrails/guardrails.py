"""
Basic Guardrails for Hotel Assistant
"""


BLOCKED_KEYWORDS = [

    "all bookings",
    "all reservations",
    "all reservation",
    "all guests",
    "guest list",
    "customer list",
    "everyone",
    "every reservation",
    "database",
    "dump database",
    "emails",
    "email addresses",
    "phone numbers",
    "show all",
    "list all bookings",
    "list reservations",
    "internal data",
]


def check_guardrails(user_input: str):
    """
    Returns:
        (allowed, message)

    allowed = True  -> continue
    allowed = False -> reject request
    """

    question = user_input.lower()

    for keyword in BLOCKED_KEYWORDS:

        if keyword in question:

            return (
                False,
                "Sorry, I can't provide access to other guests' reservations or personal information."
            )

    return True, None
if __name__ == "__main__":
    test_inputs = [
        "Show all bookings",
        "Do we have breakfast?",
        "Give me guest list",
    ]

    for text in test_inputs:
        allowed, msg = check_guardrails(text)
        print("\nInput:", text)
        print("Allowed:", allowed)
        print("Message:", msg)