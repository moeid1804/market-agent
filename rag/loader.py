from pathlib import Path
from langchain_core.documents import Document

def load_documents(data_dir:str="data"):
    documents = []
    for file_path in Path(data_dir).glob("*.txt"):
        content = file_path.read_text(encoding="utf-8")
        document = Document(
            page_content=content,
            metadata={"source": str(file_path)}
        )
        documents.append(document) 
    return documents