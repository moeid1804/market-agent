import re


MIN_RETRIEVAL_SCORE = 0.45


def validate_strategy(strategy, context, confidence):

    if confidence < MIN_RETRIEVAL_SCORE:
        raise ValueError(
            "Not enough relevant knowledge was found."
        )

    numbers = re.findall(
        r"\b\d+(?:\.\d+)?%?\b",
        strategy.model_dump_json()
    )

    unsupported_numbers = [
        number
        for number in numbers
        if number not in context
    ]

    if unsupported_numbers:
        raise ValueError(
            f"Unsupported numerical claims: {unsupported_numbers}"
        )