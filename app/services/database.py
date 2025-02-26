from pymongo import MongoClient
from datetime import datetime
import logging
from app.config import settings

class DatabaseService:
    def __init__(self):
        """Initialize MongoDB connection"""
        try:
            self.client = MongoClient(settings.mongo_uri)
            self.db = self.client.voice_assistant
            self.interactions = self.db.interactions
            # Test connection
            self.client.server_info()
            logging.info("Successfully connected to MongoDB")
        except Exception as e:
            logging.error(f"MongoDB connection error: {str(e)}")
            raise

    async def log_interaction(self, data: dict) -> bool:
        """
        Log interaction details to MongoDB
        """
        try:
            interaction = {
                "text": data["text"],
                "intent": data["intent"],
                "response": data["response_text"],
                "confidence": data["confidence"],
                "timestamp": datetime.utcnow(),
                "session_id": data.get("session_id")
            }
            self.interactions.insert_one(interaction)
            return True
        except Exception as e:
            logging.error(f"Error logging interaction: {str(e)}")
            return False