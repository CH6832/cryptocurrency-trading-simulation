#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""auth.py

Authentication services.
Handles user authentication tasks, including registration and login.
"""

import hashlib
import jwt
from datetime import datetime, timedelta

class AuthService:
    SECRET_KEY = "your_secret_key"  # Replace with a secure key in production

    async def register_user(self, user_data):
        """Registers a new user, hashes the password, and stores the user data."""
        user_data["hashed_password"] = hashlib.sha256(user_data["password"].encode()).hexdigest()
        # Insert user_data into MongoDB (not shown for brevity)
        return True

    async def login_user(self, login_data):
        """Authenticates user and returns JWT token on successful login."""
        hashed_password = hashlib.sha256(login_data["password"].encode()).hexdigest()
        # Verify credentials against MongoDB (not shown for brevity)
        if login_success:
            return jwt.encode({"user_id": "user_id"}, self.SECRET_KEY, algorithm="HS256")
        return None
