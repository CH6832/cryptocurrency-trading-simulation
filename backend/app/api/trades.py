#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""trades.py

Trade-related API endpoints.
Handles trade execution, trade history retrieval, and trading functions.
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime
from services.trading import TradingService

router = APIRouter()
trading_service = TradingService()

class TradeRequest(BaseModel):
    asset_symbol: str
    amount: float
    action: str  # 'buy' or 'sell'

@router.post("/execute")
async def execute_trade(trade: TradeRequest):
    """Executes a buy or sell trade."""
    trade_result = await trading_service.execute_trade(trade.dict())
    if trade_result:
        return trade_result
    raise HTTPException(status_code=400, detail="Trade execution failed")

@router.get("/history")
async def trade_history(user_id: str):
    """Retrieves the trade history for a specific user."""
    history = await trading_service.get_trade_history(user_id)
    return history
