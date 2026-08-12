from core.llm import get_llm
from rag.retriever import get_retriever_score
from prompts.prompt_markting import marketing_prompt
from schemas.ResponseModel import ResponseModel, LLMModel
from statistics import mean
from guardrails.validator import validate_strategy

def format_context(documents):
    context=""
    for document in documents:
        source=document.metadata.get("source", "Unknown source")
        context += (
            f"Source: {source}\n"
            f"Content: {document.page_content}\n\n"
        )
    return context

def get_sources(documents):
    sources = []

    for document in documents:
        source = document.metadata.get("source", "Unknown source")

        if source not in sources:
            sources.append(source)

    return sources



def run_agent(query:str):
    llm = get_llm()
    scores_retrieved = get_retriever_score(query)
    documents=[]
    scores=[]
    for doc, score in scores_retrieved:
        documents.append(doc)
        scores.append(score)
    confidence = round(mean(scores), 2)
    context = format_context(documents)
    sources = get_sources(documents)
   

    prompt = marketing_prompt.invoke(
        {
            "context": context,
            "query": query
        }
    )
    structured_response = llm.with_structured_output(LLMModel)
    strategy = structured_response.invoke(prompt)

    validate_strategy(
        strategy=strategy,
        context=context,
        confidence=confidence
    )

    final_response = ResponseModel(
        **strategy.model_dump(),
        source=sources,
        confidence=confidence
    )

    return final_response

if __name__ == "__main__":
    query = (
        "Create a marketing campaign for "
        "engineering students interested in IoT."
    )

    try:
        result = run_agent(query)
        print(result)

    except ValueError as error:
        print(f"Error: {error}")