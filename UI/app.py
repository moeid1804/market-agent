import sys
from pathlib import Path

import streamlit as st


# ------------------------------------------
# Project imports
# ------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(ROOT_DIR)
)


from agents.agent import run_agent


# ------------------------------------------
# Page configuration
# ------------------------------------------

st.set_page_config(
    page_title="MarketAgent",
    page_icon="🤖",
    layout="centered"
)


# ------------------------------------------
# Header
# ------------------------------------------

st.title("🤖 MarketAgent")

st.write(
    "AI Marketing Strategy Assistant powered by RAG."
)


# ------------------------------------------
# Input form
# ------------------------------------------

with st.form("marketing_form"):

    query = st.text_area(
        "What do you want to create?",
        placeholder=(
            "Create an IoT campaign "
            "for engineering students."
        ),
        height=120
    )

    submitted = st.form_submit_button(
        "Generate Strategy"
    )


# ------------------------------------------
# Generate strategy
# ------------------------------------------

if submitted:

    if not query.strip():

        st.warning(
            "Please enter a marketing request."
        )

    else:

        try:

            with st.spinner(
                "Generating strategy..."
            ):

                response = run_agent(query)


            # Save result
            st.session_state["response"] = response


        except ValueError as error:

            st.error(
                f"Guardrail: {error}"
            )


        except Exception as error:

            st.error(
                f"Error: {error}"
            )


# ------------------------------------------
# Display saved response
# ------------------------------------------

if "response" in st.session_state:

    response = st.session_state["response"]

    st.success(
        "Strategy generated successfully."
    )


    st.subheader("🎯 Target Segments")

    for segment in response.target_segments:
        st.write(f"- {segment}")


    st.subheader("📢 Campaign Strategy")

    st.write(
        response.campaign_strategy
    )


    st.subheader("📱 Channels")

    for channel in response.channels:
        st.write(f"- {channel}")


    st.subheader("💡 Content Ideas")

    for idea in response.content_ideas:
        st.write(f"- {idea}")


    st.subheader("📊 KPIs")

    for kpi in response.kpis:
        st.write(f"- {kpi}")


    st.subheader("📚 Sources")

    for source in response.source:
        st.write(f"- {source}")


    st.subheader(
        "🔎 Retrieval Confidence"
    )

    st.metric(
        "Relevance Score",
        f"{response.confidence:.2f}"
    )