import time

from app.clients.ollama_client import client

from app.core.config import DEFAULT_MODEL
from app.core.constants import (
    DEFAULT_TEMPERATURE,
    DEFAULT_TOP_P,
    MAX_TOKENS
)

from app.core.prompts import CYBER_SECURITY_PROMPT

from app.services.monitoring_service import log_interaction

from app.utils.text_cleaner import clean


def generate_response(
    prompt,
    model_id=DEFAULT_MODEL,
    temperature=DEFAULT_TEMPERATURE,
    top_p=DEFAULT_TOP_P,
    max_tokens=MAX_TOKENS,
):

    messages = [
        {
            "role": "system",
            "content": CYBER_SECURITY_PROMPT
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    start = time.time()

    response = client.chat(
        model=model_id,
        messages=messages,
        options={
            "temperature": temperature,
            "top_p": top_p,
            "num_predict": max_tokens,
        }
    )

    latency = round(time.time() - start, 2)

    output_text = response["message"]["content"]

    prompt_tokens = response.get("prompt_eval_count", 0)

    completion_tokens = response.get("eval_count", 0)

    result = {
        "model": model_id,
        "response": clean(output_text),
        "latency": latency,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": prompt_tokens + completion_tokens,
    }

    log_interaction(result)

    return result