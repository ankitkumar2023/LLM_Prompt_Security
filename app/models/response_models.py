from pydantic import BaseModel


class ModelResponse(BaseModel):

    model: str

    response: str

    latency: float

    prompt_tokens: int

    completion_tokens: int

    total_tokens: int