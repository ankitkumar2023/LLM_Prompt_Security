# models.py

import time

from ollama import Client

from utils import clean
from monitoring import log_interaction

client = Client(host="http://localhost:11434")


def invoke_model(
    model_id,
    prompt,
    system=None,
    temperature=0.7,
    top_p=0.9,
    max_tokens=512,
    stream=False,
):

    messages = []

    if system:
        messages.append({
            "role": "system",
            "content": system
        })

    messages.append({
        "role": "user",
        "content": prompt
    })

    start = time.time()

    response = client.chat(
        model=model_id,
        messages=messages,
        stream=stream,
        options={
            "temperature": temperature,
            "top_p": top_p,
            "num_predict": max_tokens,
        }
    )

    latency = round(time.time() - start, 2)

    if stream:

        final_text = ""

        for chunk in response:

            token = chunk["message"]["content"]

            print(token, end="", flush=True)

            final_text += token

        print()

        output_text = final_text

        prompt_tokens = 0
        completion_tokens = 0

    else:

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