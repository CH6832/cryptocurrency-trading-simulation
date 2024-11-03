#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""config.py

Configuration settings.
Handles configuration and environment variables.
"""

import os

class Config:
    """Configuration class to centralize environment variables."""
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    SECRET_KEY = os.getenv("SECRET_KEY", "replace_this_with_a_secure_key")

config = Config()
