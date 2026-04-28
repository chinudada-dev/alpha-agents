from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings


def get_vector_store():
    embedding = OpenAIEmbeddings()

    vectordb = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding,
    )

    return vectordb
