#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""portfolio.py

Portfolio-related API endpoints.
Provides endpoints for viewing and analyzing user portfolio data.
"""

from fastapi import APIRouter, HTTPException, Depends
from services.portfolio import PortfolioService

router = APIRouter()
portfolio_service = PortfolioService()

@router.get("/")
async def get_portfolio(user_id: str):
    """Fetches current portfolio data for a specific user."""
    portfolio = await portfolio_service.get_portfolio(user_id)
    if portfolio:
        return portfolio
    raise HTTPException(status_code=404, detail="Portfolio not found")
