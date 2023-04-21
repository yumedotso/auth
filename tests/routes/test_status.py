"""Tests for the status route."""
from http import HTTPStatus
from unittest import TestCase

from src.app import create_server


class TestStatusRoute(TestCase):
    """
    Test status routes class
    """

    def __init__(self):
        super().__init__()
        self.client = create_server().test_client()

    def test_status_returns_ok(self):
        """
        Test the status route.
        """
        response = self.client.get("/api/status/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json, {"msg": "The server is up and running"})
