from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from .config import LLM_PROVIDER, GROQ_API_KEY, GROQ_MODEL, OPENAI_API_KEY, OPENAI_MODEL

def get_llm():
    if LLM_PROVIDER == "groq":
        if not GROQ_API_KEY or not GROQ_MODEL:
            raise ValueError("Groq api or model is missing")
        
        return ChatGroq(api_key=GROQ_API_KEY,
                         model=GROQ_MODEL,
                         temperature=0)
    
    if LLM_PROVIDER == "openai":
        if not OPENAI_API_KEY or not OPENAI_MODEL:
            raise ValueError("OpenAI api or model is missing")
        return ChatOpenAI(api_key=OPENAI_API_KEY,
                           model=OPENAI_MODEL,
                           temperature=0)
if __name__ == "__main__":
    llm = get_llm()

    response = llm.invoke(
        "Say: MarketAgent LLM is working."
    )

    print(response.content)