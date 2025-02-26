from google.cloud import dialogflow
import logging
from app.config import settings

class DialogflowService:
    def __init__(self):
        """
        Initialize Dialogflow client
        """
        try:
            self.project_id = settings.dialogflow_project_id
            self.session_client = dialogflow.SessionsClient()
            logging.info("Dialogflow client initialized successfully")
        except Exception as e:
            logging.error(f"Dialogflow initialization error: {str(e)}")
            raise

    async def detect_intent(self, text: str, session_id: str, language_code: str) -> dict:
        """
        Detect intent from user input using Dialogflow
        """
        try:
            session = self.session_client.session_path(self.project_id, session_id)
            text_input = dialogflow.TextInput(text=text, language_code=language_code)
            query_input = dialogflow.QueryInput(text=text_input)

            response = self.session_client.detect_intent(
                request={"session": session, "query_input": query_input}
            )

            return {
                "intent": response.query_result.intent.display_name,
                "response_text": response.query_result.fulfillment_text,
                "confidence": response.query_result.intent_detection_confidence
            }
        except Exception as e:
            logging.error(f"Dialogflow API error: {str(e)}")
            raise