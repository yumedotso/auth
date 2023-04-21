"""User schemas module."""
from flask_marshmallow import Marshmallow

from model.user import User

ma = Marshmallow()


# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring


class UserSchema(ma.SQLAlchemyAutoSchema):

    """
    User schema class, used to serialize the user response.
    """

    # pylint: disable=too-few-public-methods

    class Meta:
        """
        Meta class for the user schema.
        """

        model = User


user_schema = UserSchema()
users_schema = UserSchema(many=True)
