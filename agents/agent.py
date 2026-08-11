from core.llm import get_llm
from rag.retriever import get_retriever
from prompts.prompt_markting import marketing_prompt

def format_context(documents):
    context=""
    for document in documents:
        source=document.metadata.get("source", "Unknown source")
        context += (
            f"Source: {source}\n"
            f"Content: {document.page_content}\n\n"
        )
    return context


def run_agent(query:str):
    retriever = get_retriever()
    llm = get_llm()
    documents = retriever.invoke(query)
    context = format_context(documents)
    prompt = marketing_prompt.invoke(
        {
            "context": context,
            "query": query
        }
    )
    response = llm.invoke(prompt)
    return response.content
if __name__ == "__main__":
    query = "Create a marketing campaign for engineering students interested in IoT."

    result = run_agent(query)

    print(result)