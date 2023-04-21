"""User routes."""
from http import HTTPStatus

from flask import Blueprint, jsonify, request

from schemas.users_schemas import user_schema, users_schema
from services.user_services import (
    create_user,
    delete_user,
    get_user,
    get_users,
    update_user,
)

user_routes = Blueprint("users", __name__)


@user_routes.route("/users", methods=["GET"])
def get_all_users():
    """
    Get all users.
    """
    users = get_users()
    users_dict = users_schema.dump(users)

    return jsonify({"data": users_dict}), HTTPStatus.OK


@user_routes.route("/users", methods=["POST"])
def create_new_user():
    """
    Create a new user.
    """
    data = request.json
    new_user = create_user(data)
    user_dict = user_schema.dump(new_user)

    return jsonify({"data": user_dict}), HTTPStatus.CREATED


@user_routes.route("/users/<string:user_id>", methods=["GET"])
def get_single_user(user_id):
    """
    Get a single user, using the user id.
    """
    user = get_user(user_id)
    user_dict = user_schema.dump(user)
    return jsonify({"data": user_dict}), HTTPStatus.OK


@user_routes.route("/users/<string:user_id>", methods=["PUT"])
def update_single_user(user_id):
    """
    Update a single user, using the user id.
    """
    data = request.json
    update_user(user_id, data)
    return jsonify({"msg": "User correctly updated"}), HTTPStatus.OK


@user_routes.route("/users/<string:user_id>", methods=["DELETE"])
def delete_single_user(user_id):
    """
    Delete a single user, using the user id.
    """
    delete_user(user_id)
    return jsonify({"msg": "User deleted"}), HTTPStatus.OK
