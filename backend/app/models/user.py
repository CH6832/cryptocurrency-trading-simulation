#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""user.py

User model schema for MongoDB.
Defines the structure and fields required to store user information.
"""

from pydantic import BaseModel, Field
from bson import ObjectId

class User(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    username: str
    email: str
    hashed_password: str

    class Config:
        """Configuration for the User model."""
        arbitrary_types_allowed = True
