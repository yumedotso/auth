"""User services"""
from sqlite3 import IntegrityError

from werkzeug.exceptions import BadRequest, NotFound

from model.db import db
from model.user import User

USER_NOT = "User not found"
MISSING_PARAMS = "Missing required parameters"


def create_user(data):
    """
    Creates a new user.
    """
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    if not all([username, password, email]):
        raise BadRequest(MISSING_PARAMS, 404)

    new_user = User(username=username, password=password, email=email)

    try:
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError as error:
        raise BadRequest("Duplicate entry") from error

    return new_user


def get_user(user_id):
    """
    Looks for a user with the given id.
    """
    user = User.query.get(user_id)
    if user is None:
        raise NotFound(USER_NOT)
    return user


def get_users():
    """
    Returns all users.
    """
    users = User.query.all()
    return users


def update_user(user_id, data):
    """
    Updates a user with the given data.
    """
    user = User.query.get(user_id)

    if user is None:
        raise NotFound(USER_NOT)

    new_user = User()

    for key in data:
        if key == "password":
            new_user.set_password(data[key])
            user[key] = new_user.password_hash
        else:
            user[key] = data[key]

    db.session.commit()


def delete_user(user_id):
    """
    Delete a user.
    """
    user = User.query.get(user_id)

    if user is None:
        raise NotFound(USER_NOT)

    db.session.delete(user)
    db.session.commit()
