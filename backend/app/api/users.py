#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""users.py

User-related API endpoints.
Includes endpoints for user registration, login, and profile management.
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from services.auth import AuthService

router = APIRouter()
auth_service = AuthService()

class UserRegistration(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

@router.post("/register")
async def register_user(user: UserRegistration):
    """Registers a new user."""
    user_created = await auth_service.register_user(user.dict())
    if user_created:
        return {"message": "User registered successfully"}
    raise HTTPException(status_code=400, detail="User registration failed")

@router.post("/login")
async def login_user(user: UserLogin):
    """Logs in an existing user."""
    token = await auth_service.login_user(user.dict())
    if token:
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid email or password")
