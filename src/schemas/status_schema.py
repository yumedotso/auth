""" Status schema module."""
from flask_marshmallow import Schema
from marshmallow.fields import Str


# pylint: disable=too-few-public-methods
class StatusSchema(Schema):
    """
    Status schema class, used to serialize the status response.
    """

    # pylint: disable=too-few-public-methods
    class Meta:
        """Meta class for the status schema."""

        fields = ["msg"]

    msg = Str()
