"""Module imports"""
from http import HTTPStatus

from flasgger import swag_from
from flask import Blueprint, jsonify

status_blueprint = Blueprint("status", __name__)


@status_blueprint.route("/", methods=["GET"])
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": "The server is up and running",
                "schema": {"msg": "The server is up and running"},
            }
        }
    }
)
def status():
    """
    Check if the server is up and running.

    Returns:
        msg (str): The server is up and running.
    """
    return jsonify({"msg": "The server is up and running"})
