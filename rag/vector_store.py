from functools import lru_cache
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from .loader import load_documents
from .chunking import split_documents
from .embedding import get_embedding

QDRANT_PATH = "qdrant_db"
COLLECTION_NAME = "my_collection"

def create_vector_store():
    documents = load_documents()
    chunked_documents = split_documents(documents)
    embeddings = get_embedding()
    vector_store = QdrantVectorStore.from_documents(
        documents=chunked_documents,
        embedding=embeddings,
        path=QDRANT_PATH,
        collection_name=COLLECTION_NAME,
        
    )
    return vector_store
@lru_cache(maxsize=1)
def get_vector_store():
    embeddings = get_embedding()
    client = QdrantClient(path=QDRANT_PATH)
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embeddings
    )
    return vector_store


    

if __name__ == "__main__":
    vectorstore = create_vector_store()
    print("Vector store built successfully.")
    vectorstore.client.close()