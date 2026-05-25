# safety.py

from ollama import Client
from config import SAFETY_MODEL

client = Client(host="http://localhost:11434")

SAFETY_POLICY = """
You are a safety classifier.

Classify the request as:

SAFE
or
UNSAFE

If unsafe, explain why.
"""


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