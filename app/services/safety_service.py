from app.clients.ollama_client import client

from app.core.config import SAFETY_MODEL

from app.core.prompts import SAFETY_POLICY


def safety_check(user_prompt):

    response = client.chat(
        model=SAFETY_MODEL,
        messages=[
            {
                "role": "system",
                "content": SAFETY_POLICY
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        options={
            "temperature": 0,
            "num_predict": 100,
        }
    )

    return response["message"]["content"]