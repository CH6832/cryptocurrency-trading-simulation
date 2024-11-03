#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""tests_users.py

Tests for user-related API endpoints.
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user():
    """Tests user registration."""
    response = client.post("/api/users/register", json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}

def test_login_user():
    """Tests user login."""
    response = client.post("/api/users/login", json={
        "email": "testuser@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
