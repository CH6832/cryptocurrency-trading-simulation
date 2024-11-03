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
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
# origins = ["*"]  # Set to ["http://localhost", "http://localhost:8000"] in production
origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
