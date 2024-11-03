#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""mongodb.py

MongoDB connection setup.
Handles MongoDB client setup, connection, and disconnection for the application.
"""

from motor.motor_asyncio import AsyncIOMotorClient
import os
from config import Config

# MongoDB URI and client setup
# MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
CONFIGS = Config()
client = AsyncIOMotorClient(CONFIGS.MONGO_URI)
db = client.trading_simulation

# Collections
users_collection = db.get_collection("users")
trades_collection = db.get_collection("trades")
portfolio_collection = db.get_collection("portfolio")
notifications_collection = db.get_collection("notifications")

async def connect_db():
    """Establishes MongoDB connection (placeholder for additional setup if needed)."""
    print("Connecting to MongoDB...")

async def disconnect_db():
    """Disconnects from MongoDB."""
    print("Disconnecting from MongoDB...")
    client.close()
