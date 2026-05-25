# config.py

MODELS = {
    "qwen": "qwen2.5:1.5b",
    "llama": "llama3.2:3b",
    "gemma": "gemma3:1b",
}

DEFAULT_MODEL = MODELS["qwen"]

SAFETY_MODEL = "llama-guard3:8b"