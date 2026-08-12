from agents.agent import run_agent
from .test_cases import TEST_CASES


passed_tests = 0


for test in TEST_CASES:
    print(f"\nRunning: {test['name']}")

    try:
        response = run_agent(test["query"])
        response_text = response.model_dump_json().lower()

        if test["hallucination"]:
            handled_safely = (
                "unavailable" in response_text
                or "no data" in response_text
            )

            if handled_safely:
                print("PASS ✅")
                passed_tests += 1
            else:
                print("FAIL ❌")

        else:
            expected_words = test["expected"]

            all_found = all(
                word.lower() in response_text
                for word in expected_words
            )

            if all_found:
                print("PASS ✅")
                passed_tests += 1
            else:
                print("FAIL ❌")

    except ValueError:
        if test["hallucination"]:
            print("PASS ✅ - Guardrail triggered")
            passed_tests += 1
        else:
            print("FAIL ❌")


print(f"\nResult: {passed_tests}/{len(TEST_CASES)} passed")