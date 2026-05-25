from ollama import Client

from app.core.config import OLLAMA_HOST

client = Client(host=OLLAMA_HOST)