from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the OLLAMA_MODEL and MAX_HISTORY from environment variables
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")
MAX_HISTORY = int(os.getenv("MAX_HISTORY", 6))

MEMORY_FILE = "Data/Memory/chat_history.json"
DOCS_FOLDER = "Data/Docs"
