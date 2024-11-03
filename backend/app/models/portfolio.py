#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Portfolio model schema for MongoDB.
Defines the structure and fields required to store portfolio data.
"""

from pydantic import BaseModel, Field
from bson import ObjectId

class Portfolio(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    user_id: ObjectId
    assets: dict  # {"BTC": 0.5, "ETH": 2}

    class Config:
        """Configuration for the Portfolio model."""
        arbitrary_types_allowed = True
