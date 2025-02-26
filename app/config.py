from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application settings
    """
    app_name: str = "intent"
    debug_mode: bool = False
    dialogflow_project_id: str = "intent-452116"
    google_credentials_path: str = "E:/intent/google_credentials.json"
    mongo_uri: str = "mongodb://localhost:27017"

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()