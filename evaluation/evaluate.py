from agents.agent import run_agent
from evaluation.test_cases import TEST_CASES


passed_tests = 0


for test in TEST_CASES:

    print(f"\nRunning: {test['name']}")

    try:

        response = run_agent(test["query"])

        response_text = response.model_dump_json().lower()




        expected_ok = all(
            term.lower() in response_text
            for term in test["expected_terms"]
        )



        forbidden_ok = all(
            term.lower() not in response_text
            for term in test["forbidden_terms"]
        )


        structure_ok = (
            bool(response.target_segments)
            and bool(response.campaign_strategy)
            and bool(response.channels)
            and bool(response.content_ideas)
            and bool(response.kpis)
        )


 

        if expected_ok and forbidden_ok and structure_ok:

            print("PASS ✅")
            passed_tests += 1

        else:

            print("FAIL ❌")

            if not expected_ok:
                print("  Missing expected content")

            if not forbidden_ok:
                print("  Unsupported claim appeared")

            if not structure_ok:
                print("  Invalid response structure")


    except ValueError as error:

        if test["allow_guardrail"]:

            print(f"PASS ✅ - Guardrail triggered: {error}")
            passed_tests += 1

        else:

            print(f"FAIL ❌ - Unexpected guardrail: {error}")


    except Exception as error:

        print(f"ERROR ❌ - {error}")


print(
    f"\nResult: {passed_tests}/{len(TEST_CASES)} passed"
)