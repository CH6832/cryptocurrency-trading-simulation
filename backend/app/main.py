#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""main.py

Main entry point for the FastAPI application.
Defines the FastAPI instance, configures routes, and includes CORS setup.

Run the backend server:
uvicorn main:app --reload --host 127.0.0.1 --port 8000

To read the docs, go to:
http://127.0.0.1:8000/docs
"""

import os
import sys
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # Use FastAPI's CORSMiddleware
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Import API routers and database functions
try:
    from api import users, trades, portfolio
    from database.mongodb import connect_db, disconnect_db
except ImportError as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)

# Initialize FastAPI app
app = FastAPI(title="Crypto Trading Simulation API")

# CORS configuration for frontend and other origins during testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Event handlers for database connection management
@app.on_event("startup")
async def startup_event():
    """Handle startup event to connect to the database."""
    await connect_db()

@app.on_event("shutdown")
async def shutdown_event():
    """Handle shutdown event to disconnect from the database."""
    await disconnect_db()

# Include API routers with prefixes
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(trades.router, prefix="/api/trades", tags=["Trades"])
app.include_router(portfolio.router, prefix="/api/portfolio", tags=["Portfolio"])

# Root health check endpoint
@app.get("/")
async def root():
    """Health check endpoint."""
    return {"message": "Crypto Trading Simulation API is running"}

@app.get("/crypto")
async def get_crypto_price(crypto_name: str):
    """
    Fetch the current price of a given cryptocurrency from CoinGecko API.
    
    Arguments:
    crypto_name: The name of the cryptocurrency (e.g., bitcoin, ethereum).
    
    Returns:
    A JSON response with the current price in USD.
    """
    try:
        # Construct the CoinGecko API URL dynamically based on the provided crypto_name
        COINGECKO_API_URL = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_name}&vs_currencies=usd'
        
        # Make the request to the CoinGecko API
        response = requests.get(COINGECKO_API_URL)
        data = response.json()

        # Check if the cryptocurrency data is available in the response
        if crypto_name not in data:
            raise HTTPException(status_code=404, detail=f"Price data for {crypto_name} not found")

        # Return the price of the cryptocurrency
        return data[crypto_name]
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")

@app.get("/crypto/all")
async def get_all_crypto_prices():
    """
    Fetch prices for Bitcoin, Ethereum, and Litecoin from CoinGecko API.
    
    Returns:
    A JSON response with the current prices in USD for all the cryptocurrencies.
    """
    try:
        # CoinGecko API URL to get the prices of Bitcoin, Ethereum, and Litecoin
        COINGECKO_API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin&vs_currencies=usd'

        # Request prices from CoinGecko API
        response = requests.get(COINGECKO_API_URL)
        data = response.json()

        # Log the full response for debugging
        print("CoinGecko All Crypto Response:", data)

        # Return the cryptocurrency prices for all three cryptocurrencies
        return data

    except requests.exceptions.RequestException as e:
        # Log the error and return a 500 error
        print(f"Error fetching data: {e}")
        raise HTTPException(status_code=500, detail="Error fetching cryptocurrency data")
