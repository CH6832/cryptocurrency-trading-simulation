#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""portfolio.py

Portfolio service.
Handles all operations related to the user's portfolio, such as retrieval and updates.
"""

from datetime import datetime
from models.portfolio import Portfolio
from database.mongodb import portfolio_collection

class PortfolioService:
    async def get_portfolio(self, user_id):
        """Retrieves the portfolio for a given user."""
        portfolio = await portfolio_collection.find_one({"user_id": user_id})
        if portfolio:
            return Portfolio(**portfolio).dict()
        else:
            # Return an empty portfolio structure if none exists
            return {"user_id": user_id, "assets": {}}

    async def update_portfolio(self, user_id, asset, amount, action):
        """
        Updates user portfolio based on trade action.

        Args:
            user_id (str): ID of the user whose portfolio to update.
            asset (str): Asset symbol to update (e.g., "BTC").
            amount (float): Amount to update in portfolio.
            action (str): Either "buy" or "sell" to determine the portfolio change.
        """
        portfolio = await portfolio_collection.find_one({"user_id": user_id})
        
        # Initialize portfolio if it doesn't exist
        if not portfolio:
            portfolio = Portfolio(user_id=user_id, assets={})
        else:
            portfolio = Portfolio(**portfolio)

        # Update asset holdings based on action
        if action == "buy":
            portfolio.assets[asset] = portfolio.assets.get(asset, 0) + amount
        elif action == "sell":
            if portfolio.assets.get(asset, 0) >= amount:
                portfolio.assets[asset] -= amount
            else:
                raise ValueError(f"Not enough {asset} to sell.")

        # Save updated portfolio
        await portfolio_collection.replace_one({"user_id": user_id}, portfolio.dict(by_alias=True), upsert=True)
        return portfolio.dict()
