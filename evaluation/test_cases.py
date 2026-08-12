TEST_CASES = [
    {
        "name": "IoT student campaign",
        "query": "Create a marketing campaign for engineering students building IoT projects.",
        "expected": ["engineering", "iot"],
        "hallucination": False,
    },
    {
        "name": "Maker campaign",
        "query": "Create a campaign for makers and hardware hobbyists.",
        "expected": ["maker"],
        "hallucination": False,
    },
    {
        "name": "Prototype builder campaign",
        "query": "Create a campaign for people who have a hardware idea and want to build a prototype.",
        "expected": ["prototype"],
        "hallucination": False,
    },
    {
        "name": "Fake conversion rate",
        "query": "Create a campaign based on Mokwn's previous 25% conversion rate.",
        "expected": [],
        "hallucination": True,
    },
    {
        "name": "Fake customer count",
        "query": "Create a campaign based on Mokwn having 50000 customers.",
        "expected": [],
        "hallucination": True,
    },
]