from app.services.inference_service import generate_response


def test_generation():

    result = generate_response(
        prompt="What is machine learning?"
    )

    assert "response" in result