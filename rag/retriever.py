from .vector_store import create_vector_store, get_vector_store

def get_retriever():
    vectore_store = get_vector_store()
    return vectore_store.as_retriever(
        search_kwargs={"k": 3}
    )
if __name__ == "__main__":
    retriever = get_retriever()

    documents = retriever.invoke(
        "What products are useful for IoT projects?"
    )

    for document in documents:
        print(document.metadata)
        print(document.page_content)
        print("-" * 50)

    retriever.vectorstore.client.close()