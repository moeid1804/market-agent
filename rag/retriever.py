from rag.vector_store import get_vector_store


def get_retriever_score(query, k=3):
    vector_store = get_vector_store()

    try:
        results = vector_store.similarity_search_with_relevance_scores(
            query,
            k=k
        )

        return results

    finally:
        vector_store.client.close()