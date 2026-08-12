# MarketAgent

MarketAgent is a **RAG-powered AI Marketing Strategy Assistant** built for Mokwn.

It uses Mokwn business knowledge to generate structured marketing strategies, analyze customer segments, recommend channels and content ideas, and reduce unsupported AI claims.

## Architecture

```text
Mokwn Knowledge Base
        ↓
Document Loader
        ↓
Text Splitter
        ↓
Hugging Face Embeddings
        ↓
Qdrant Vector Database
        ↓
User Query
        ↓
Retriever
        ↓
Relevant Context + Scores
        ↓
System Prompt + Few-shot Examples
        ↓
Groq / OpenAI LLM
        ↓
Pydantic Structured Output
        ↓
Guardrails
        ↓
Marketing Response
```

## Main Technologies

* Python
* LangChain
* Qdrant
* Hugging Face Sentence Transformers
* `all-MiniLM-L6-v2`
* Groq
* OpenAI
* Pydantic
* Streamlit
* RAG
* Prompt Engineering

## Knowledge Base

The current Mokwn knowledge base contains:

```text
data/
├── company.txt
├── products.txt
├── customer_personas.txt
└── brand_guidelines.txt
```

## Embeddings

The project uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

It converts text into **384-dimensional vectors** used for semantic search.

## Vector Database

**Qdrant** stores document embeddings and retrieves the most relevant knowledge for each user query.

The vector database is built once:

```bash
python -m rag.vector_store
```

## Run the Agent

```bash
python -m agents.agent
```

Example request:

```text
Create a marketing campaign for engineering students interested in IoT.
```

The agent returns structured data such as:

```text
target_segments
campaign_strategy
channels
content_ideas
kpis
sources
confidence
```

`confidence` represents **retrieval relevance**, not the probability that the final LLM answer is correct.

## Guardrails

MarketAgent includes basic guardrails to reduce hallucinations.

It checks retrieval relevance and prevents unsupported numerical business claims such as invented customer counts, conversion rates, or campaign results.

The system prompt also instructs the model to distinguish recommendations from actual Mokwn facts.

## Evaluation

The project includes realistic test cases for:

```text
Campaign generation
Customer segmentation
Prototype-builder targeting
Unsupported conversion rates
Unsupported customer numbers
```

Run evaluation with:

```bash
python -m evaluation.evaluate
```

## User Interface

The Streamlit interface can be started with:

```bash
streamlit run ui/app.py
```

## LLM Providers

The project supports:

```text
Groq   → development and fast inference
OpenAI → alternative supported provider
```

The provider can be changed through configuration without changing the main agent workflow.

## Project Goal

MarketAgent demonstrates how **RAG, vector search, prompt engineering, structured output, guardrails, and evaluation** can be combined to build a practical AI application instead of a simple chatbot.

## Future Improvements

For production, MarketAgent can be extended with PostgreSQL business data, hosted Qdrant, FastAPI, authentication, monitoring, caching, and live product/order/campaign analytics.
