def mask_name(name: str) -> str:
    """
    Mask guest name.

    Example:
    Nivetha -> N******
    John -> J***
    """

    if not name:
        return ""

    return name[0] + "*" * (len(name) - 1)


def mask_email(email: str) -> str:
    """
    Mask email address.

    Example:
    nivetha@gmail.com
    ->
    niv****@gmail.com
    """

    if "@" not in email:
        return email

    username, domain = email.split("@")

    if len(username) <= 3:
        masked = username[0] + "***"
    else:
        masked = username[:3] + "****"

    return f"{masked}@{domain}"