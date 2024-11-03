#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""trade.py

Trade model schema for MongoDB.
Defines the structure and fields required to store trade data.
"""

from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime

class Trade(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    user_id: ObjectId
    asset_symbol: str
    action: str  # 'buy' or 'sell'
    amount: float
    price: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        """Configuration for the Trade model."""
        arbitrary_types_allowed = True
