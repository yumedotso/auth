"""Password class"""
from werkzeug.security import check_password_hash, generate_password_hash


class Password:
    """Class to handle password hashing and checking"""

    def __init__(self, password: str):
        self.value = password

    def set_password(self):
        """Set the password hash for the user"""  # noqa: DAR101
        return generate_password_hash(self.value)

    def check_password(self, password_hash):
        """Check the password hash for the user"""
        return check_password_hash(password_hash, self.value)
