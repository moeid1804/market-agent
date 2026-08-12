import sys
from pathlib import Path

import streamlit as st


# --------------------------------------------------
# Allow Streamlit to import project modules
# --------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="MarketAgent",
    page_icon="🤖",
    layout="centered",
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🤖 MarketAgent")

st.write(
    "AI Marketing Strategy Assistant powered by RAG."
)


# --------------------------------------------------
# User input
# --------------------------------------------------

query = st.text_area(
    "What do you want to create?",
    placeholder="Create an IoT campaign for engineering students.",
    height=120,
)


# --------------------------------------------------
# Generate strategy
# --------------------------------------------------

if st.button("Generate Strategy"):

    if not query.strip():

        st.warning(
            "Please enter a marketing request."
        )

    else:

        try:

            # Import the agent only when needed
            from agents.agent import run_agent

            with st.spinner("Generating strategy..."):

                response = run_agent(query)


            # --------------------------------------
            # Success message
            # --------------------------------------

            st.success(
                "Strategy generated successfully."
            )


            # --------------------------------------
            # Target segments
            # --------------------------------------

            st.subheader("🎯 Target Segments")

            for segment in response.target_segments:

                st.write(
                    f"- {segment}"
                )


            # --------------------------------------
            # Campaign strategy
            # --------------------------------------

            st.subheader("📢 Campaign Strategy")

            st.write(
                response.campaign_strategy
            )


            # --------------------------------------
            # Channels
            # --------------------------------------

            st.subheader("📱 Channels")

            for channel in response.channels:

                st.write(
                    f"- {channel}"
                )


            # --------------------------------------
            # Content ideas
            # --------------------------------------

            st.subheader("💡 Content Ideas")

            for idea in response.content_ideas:

                st.write(
                    f"- {idea}"
                )


            # --------------------------------------
            # KPIs
            # --------------------------------------

            st.subheader("📊 KPIs")

            for kpi in response.kpis:

                st.write(
                    f"- {kpi}"
                )


            # --------------------------------------
            # Sources
            # --------------------------------------

            st.subheader("📚 Sources")

            for source in response.source:

                st.write(
                    f"- {source}"
                )


            # --------------------------------------
            # Retrieval confidence
            # --------------------------------------

            st.subheader("🔎 Retrieval Confidence")

            st.metric(
                label="Relevance Score",
                value=f"{response.confidence:.2f}",
            )


        except ValueError as error:

            st.error(
                f"Guardrail: {error}"
            )


        except Exception as error:

            st.error(
                f"Error: {error}"
            )