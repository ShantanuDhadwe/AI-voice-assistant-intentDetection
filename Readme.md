# AI Voice Assistant

A FastAPI-based voice assistant that processes text input using Dialogflow for natural language understanding.

## Features

- Text to Intent Processing using Dialogflow
- MongoDB Integration for conversation logging
- Docker containerization
- RESTful API endpoints

## Technology Stack

- FastAPI
- Dialogflow
- MongoDB
- Docker

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Root endpoint |
| `/health` | GET | Health check endpoint |
| `/process-text` | POST | Process text input |

## Setup Instructions

### Local Setup

1. Clone the repository
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up environment variables in `.env` file:
    ```env
    APP_NAME="Intent Detection"
    DEBUG_MODE=True
    DIALOGFLOW_PROJECT_ID="your-project-id"
    GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
    MONGO_URI="mongodb://localhost:27017"
    ```
4. Run the application:
    ```bash
    python run.py
    ```

### Docker Setup

1. Pull from DockerHub:
    ```bash
    docker pull shantanu454/intent-detection:latest
    ```
2. Run the container:
    ```bash
    docker run -p 8000:8000 shantanu454/intent-detection:latest
    ```

## Usage Examples

### Health Check

```bash
curl http://localhost:8000/health
```

### Process Text

```bash
curl -X POST http://localhost:8000/process-text \
     -H "Content-Type: application/json" \
     -d '{"text": "hello", "language_code": "en-US"}'
```

### Example Responses

## Health Check Response 

```JSON
{
   "status": "healthy"
}
```
##Process text Response

```JSON
{
    "intent": "greeting",
    "response_text": "Hello! How can I help you today?",
    "confidence": 0.9
}
```

###Project Structure

```
intent_detection/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py
│   └── services/
│       ├── __init__.py
│       ├── dialogflow.py
│       └── database.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

##Available Intents 

-Greeting: Hello, Hi, Hey
-Weather: What's the weather, Temperature
-Help: I need help, Help me
-Farewell: Goodbye, Bye

###Docker Commands

```bash
# View running containers
docker ps

# Stop container
docker stop <container_id>

# View logs
docker logs <container_id>

# Enter container shell
docker exec -it <container_id> bash
```
###Troubleshooting

##Connection Issues

-Verify MongoDB is running
-Check Dialogflow credentials
-Ensure ports are available

##Docker Issues

-Ensure Docker Desktop is running
-Check port mappings
-Verify environment variables
