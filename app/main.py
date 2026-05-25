from rich import print

from app.services.safety_service import safety_check
from app.services.inference_service import generate_response


def safe_generate(prompt):

    print("\n[cyan]Checking safety...[/cyan]")

    safety_result = safety_check(prompt)

    print("\n[yellow]Safety Result:[/yellow]")
    print(safety_result)

    if "UNSAFE" in safety_result.upper():

        print("\n[red]BLOCKED BY SAFETY SYSTEM[/red]")
        return

    print("\n[green]Generating Response...[/green]\n")

    result = generate_response(prompt)

    print(result["response"])

    print("\n[bold]--- METRICS ---[/bold]")
    print(f"Latency: {result['latency']} sec")
    print(f"Tokens: {result['total_tokens']}")


if __name__ == "__main__":

    prompt = input("Enter Prompt: ")

    safe_generate(prompt)