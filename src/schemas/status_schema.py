""" Status schema module."""
from flask_marshmallow import Schema
from marshmallow.fields import Str


class StatusSchema(Schema):
    """
    Status schema class, used to serialize the status response.
    """

    class Meta:
        """Meta class for the status schema."""

        fields = ["msg"]

    msg = Str()
