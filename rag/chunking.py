from langchain_text_splitters import RecursiveCharacterTextSplitter
def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    split_docs = text_splitter.split_documents(documents)
    return split_docs
if __name__ == "__main__":
    from rag.loader import load_documents

    documents = load_documents()
    chunks = split_documents(documents)

    print("Documents:", len(documents))
    print("Chunks:", len(chunks))

    for chunk in chunks:
        print(chunk.metadata)
        print(chunk.page_content)
        print("-" * 50)