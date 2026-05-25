import os

from dotenv import load_dotenv

load_dotenv()

OLLAMA_HOST = os.getenv("OLLAMA_HOST")

LOG_PATH = os.getenv("LOG_PATH")

MODELS = {
    "qwen": "qwen2.5:1.5b",
    "llama": "llama3.2:3b",
    "gemma": "gemma3:1b",
}

DEFAULT_MODEL = MODELS["qwen"]

SAFETY_MODEL = "llama-guard3:8b"