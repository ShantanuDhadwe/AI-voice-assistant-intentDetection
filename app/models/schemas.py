from pydantic import BaseModel
from typing import Optional

class VoiceRequest(BaseModel):
    """
    Schema for incoming voice/text requests
    """
    text: str
    session_id: Optional[str] = None
    language_code: str = "en-US"

class VoiceResponse(BaseModel):
    """
    Schema for API responses
    """
    intent: str
    response_text: str
    confidence: float