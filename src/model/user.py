"""User model module."""
import uuid

from flask_sqlalchemy import SQLAlchemy

from model.password import Password

db = SQLAlchemy()


class User(db.Model):
    """User model class."""

    __tablename__ = "users"

    id = db.Column(
        db.String(128),
        primary_key=True,
        unique=True,
        nullable=False,
        default=str(uuid.uuid4()),
    )
    username = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )

    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.email = email

    def set_password(self, password):
        """
        Updates the password hash for the user.
        """
        self.password_hash = Password(password).set_password()

    def check_password(self, password):
        """
        Checks the password hash for the user.
        """
        return Password(self.password_hash).check_password(password)
