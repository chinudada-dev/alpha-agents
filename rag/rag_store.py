from pathlib import Path

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def get_vector_store():
    embedding = OpenAIEmbeddings()

    vectordb = Chroma(
        persist_directory=str(PROJECT_ROOT / "chroma_db"),
        embedding_function=embedding,
    )

    return vectordb
