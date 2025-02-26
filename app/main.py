# app/main.py

from fastapi import FastAPI, HTTPException
from app.config import settings
from app.models.schemas import VoiceRequest, VoiceResponse
from app.services.dialogflow import DialogflowService
import logging
import uuid
from app.services.database import DatabaseService

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = FastAPI(
    title=settings.app_name,
    description="AI Voice Assistant using Dialogflow",
    version="1.0.0"
)

# Initialize Dialogflow service
try:
    dialogflow_service = DialogflowService()
except Exception as e:
    logging.error(f"Error initializing Dialogflow service: {str(e)}")
    raise

try:
    db_service = DatabaseService()
except Exception as e:
    logging.error(f"Error initializing Database service: {str(e)}")
    raise

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/process-text", response_model=VoiceResponse)
async def process_text(request: VoiceRequest):
    try:
        session_id = request.session_id or str(uuid.uuid4())
        
        result = await dialogflow_service.detect_intent(
            text=request.text,
            session_id=session_id,
            language_code=request.language_code
        )

        # Log the interaction
        await db_service.log_interaction({
            "text": request.text,
            "session_id": session_id,
            **result
        })

        return VoiceResponse(
            intent=result["intent"],
            response_text=result["response_text"],
            confidence=result["confidence"]
        )

    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Error processing text input"
        )