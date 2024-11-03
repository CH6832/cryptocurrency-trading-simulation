#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""test_portfolio.py

Tests for portfolio-related API endpoints.
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_portfolio():
    """Tests retrieval of portfolio data."""
    response = client.get("/api/portfolio", params={"user_id": "user_id_example"})
    assert response.status_code == 200
    assert "assets" in response.json()
