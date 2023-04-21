"""This module creates a flask app instance and registers the blueprints"""
from flasgger import Swagger
from flask import Flask
from flask_cors import CORS

from routes.status import status_blueprint


# @defintion: create_server
def create_server():
    """
    Create a Flask app instance with CORS and Swagger documentation.

    Returns:
        app (Flask): The Flask app instance.
    """
    app = Flask(__name__)

    CORS(app)

    app.register_blueprint(status_blueprint, url_prefix="/api/status")

    app.config["SWAGGER"] = {
        "title": "Yume auth API",
        "description": "Yume auth micro-service, security and authentication",
        "version": "1.0",
    }

    app.config["NAME"] = "Yume auth API"

    Swagger(app)

    return app


if __name__ == "__main__":
    server = create_server()
    server.run(host="0.0.0.0", port=3001, debug=True)
