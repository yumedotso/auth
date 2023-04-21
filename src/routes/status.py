"""Module imports"""
from http import HTTPStatus

from flasgger import swag_from
from flask import Blueprint, jsonify

from src.schemas.status_schema import StatusSchema

status_blueprint = Blueprint("status", __name__)

SERVER_SETUP_MESSAGE = "The server is up and running"


@status_blueprint.route("/", methods=["GET"])
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": SERVER_SETUP_MESSAGE,
                "schema": StatusSchema,
            }
        }
    }
)
def check_server_status():
    """
    Check if the server is up and running.

    Returns:
        msg (str): The server is up and running.
    """
    return jsonify({"msg": SERVER_SETUP_MESSAGE}), HTTPStatus.OK
