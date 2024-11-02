#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""setup_db.py

This script initializes the MongoDB database for the crypto trading simulation application.
It creates necessary collections and optionally seeds initial data for testing and development purposes.
"""

import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

def connect_to_mongo(uri: str):
    """Connect to MongoDB using the provided URI."""
    try:
        client = MongoClient(uri)
        # Attempt to access the server to ensure the connection is successful
        client.admin.command('ping')  # This will raise an error if the connection fails
        print("Successfully connected to MongoDB!")
        return client
    except ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}")
        return None

def create_collections(db):
    """Create collections in the MongoDB database if they don't exist."""
    # List of collections to create
    collections = ['users', 'trades', 'portfolio']

    for collection_name in collections:
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
            print(f"Collection '{collection_name}' created.")
        else:
            print(f"Collection '{collection_name}' already exists.")

def seed_initial_data(db):
    """Seed the database with initial data (optional)."""
    # Example data for seeding
    users_data = [
        {"username": "admin", "email": "admin@example.com", "password": "hashed_password"},
        {"username": "trader1", "email": "trader1@example.com", "password": "hashed_password"},
    ]

    # Insert users data if the collection is empty
    users_collection = db['users']
    if users_collection.count_documents({}) == 0:
        users_collection.insert_many(users_data)
        print("Initial user data seeded.")
    else:
        print("Users collection already has data; skipping seeding.")

def main():
    """Main function to execute the database setup process.
    Connects to MongoDB, creates necessary collections, and seeds initial data.
    """
    # Load environment variables for MongoDB connection
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/mydatabase")

    # Connect to MongoDB
    client = connect_to_mongo(mongo_uri)
    if client:
        # Create or access the database
        db_name = mongo_uri.split("/")[-1]  # Extract database name from URI
        db = client[db_name]

        # Create necessary collections
        create_collections(db)

        # Optionally seed the database with initial data
        seed_initial_data(db)

        # Close the MongoDB connection
        client.close()
        print("Database setup completed successfully!")

if __name__ == "__main__":
    main()
