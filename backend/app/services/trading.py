#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""trading.py

Trading service.
Handles the core trading logic, including trade execution, historical data retrieval, 
and portfolio management.
"""

from datetime import datetime
from models.trade import Trade
from models.portfolio import Portfolio
from database.mongodb import trades_collection, portfolio_collection

class TradingService:
    async def execute_trade(self, trade_data):
        """Executes a trade and updates the user's portfolio accordingly."""
        trade = Trade(**trade_data, timestamp=datetime.utcnow())
        
        # Insert trade into the database
        await trades_collection.insert_one(trade.dict(by_alias=True))

        # Update portfolio based on trade action
        action = trade_data.get("action").lower()
        asset = trade_data.get("asset_symbol")
        amount = trade_data.get("amount")
        await self.update_portfolio(trade.user_id, asset, amount, action)
        
        return trade.dict()

    async def update_portfolio(self, user_id, asset, amount, action):
        """Updates user portfolio based on trade action."""
        portfolio = await portfolio_collection.find_one({"user_id": user_id})
        if not portfolio:
            portfolio = Portfolio(user_id=user_id, assets={})

        # Update asset holdings based on action
        if action == "buy":
            portfolio.assets[asset] = portfolio.assets.get(asset, 0) + amount
        elif action == "sell":
            portfolio.assets[asset] = portfolio.assets.get(asset, 0) - amount

        # Save updated portfolio
        await portfolio_collection.replace_one({"user_id": user_id}, portfolio.dict(by_alias=True), upsert=True)

    async def get_trade_history(self, user_id):
        """Retrieves the trade history for a given user."""
        trades = await trades_collection.find({"user_id": user_id}).to_list(None)
        return [trade for trade in trades]
