# app.py

from config import DEFAULT_MODEL
from models import invoke_model
from safety import safety_check


def safe_generate(prompt):

    print("\\nChecking safety...")

    safety = safety_check(prompt)

    print("\\nSafety Result:")
    print(safety)

    if "UNSAFE" in safety.upper():

        print("\\nBLOCKED BY SAFETY SYSTEM")

        return

    print("\\nGenerating Response...\\n")

    result = invoke_model(
        model_id=DEFAULT_MODEL,
        prompt=prompt,
        system="You are a cybersecurity instructor.",
        temperature=0.7,
        max_tokens=300,
    )

    print(result["response"])

    print("\\n--- METRICS ---")
    print(f"Latency: {result['latency']} sec")
    print(f"Tokens: {result['total_tokens']}")


if __name__ == "__main__":

    prompt = input("Enter Prompt: ")

    safe_generate(prompt)