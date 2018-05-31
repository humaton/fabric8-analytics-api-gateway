"""Unit tests for the authorization module."""
import json
from unittest import TestCase
from gateway import auth
from gateway.api_v1 import app

class TestAuth(TestCase):
    """Test that endpoint is set from the right key:value pair."""

    def setUp(self):
        """Set it up."""
        self.app = app.test_client()

    def test_fetch_public_key(self):
        """Test list of supported services."""
        with self.assertRaises(Exception):
            _=auth.fetch_public_key

    def test_decode_token(self):
        """Test list of supported services."""
        with self.assertRaises(Exception):
            _=auth.decode_token

    def test_login_required(self):
        """Test list of supported services."""
        with self.assertRaises(Exception):
            _=auth.decode_token
