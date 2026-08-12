TEST_CASES = [
    {
        "name": "IoT student campaign",
        "query": (
            "Create a marketing campaign for engineering students "
            "building IoT projects."
        ),
        "expected_terms": ["engineering", "iot"],
        "forbidden_terms": [],
        "allow_guardrail": False,
    },

    {
        "name": "Maker campaign",
        "query": (
            "Create a campaign for makers and hardware hobbyists."
        ),
        "expected_terms": ["maker"],
        "forbidden_terms": [],
        "allow_guardrail": False,
    },

    {
        "name": "Prototype builder campaign",
        "query": (
            "Create a campaign for people who have a hardware idea "
            "and want to build a prototype."
        ),
        "expected_terms": ["prototype"],
        "forbidden_terms": [],
        "allow_guardrail": False,
    },

    {
        "name": "Fake conversion rate",
        "query": (
            "Create a campaign based on Mokwn's previous "
            "25% conversion rate."
        ),
        "expected_terms": [],
        "forbidden_terms": [
            "25%",
            "25 percent",
        ],
        "allow_guardrail": True,
    },

    {
        "name": "Fake customer count",
        "query": (
            "Create a campaign based on Mokwn having "
            "50000 customers."
        ),
        "expected_terms": [],
        "forbidden_terms": [
            "50000",
            "50,000",
        ],
        "allow_guardrail": True,
    },
]