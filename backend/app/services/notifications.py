#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""notifications.py

Notification service.
Handles notification logic, such as sending trade confirmations and portfolio updates.
"""

from models.user import User
from database.mongodb import notifications_collection

class NotificationService:
    async def send_trade_confirmation(self, user_id, trade_details):
        """Sends a trade confirmation to the user."""
        notification = {
            "user_id": user_id,
            "message": f"Trade confirmed: {trade_details}",
            "timestamp": datetime.utcnow()
        }
        await notifications_collection.insert_one(notification)
        return notification

    async def get_notifications(self, user_id):
        """Fetches notifications for a given user."""
        notifications = await notifications_collection.find({"user_id": user_id}).to_list(None)
        return notifications
