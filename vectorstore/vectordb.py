from langchain_community.vectorstores import FAISS

def create_vector_store(documents, embedding_model):
    vectorstore = FAISS.from_documents(documents, embedding_model)
    return vectorstore


def save_vector_store(vectorstore, path="faiss_index"):
    vectorstore.save_local(path)


def load_vector_store(embedding_model, path="faiss_index"):
    return FAISS.load_local(
        path,
        embedding_model,
        allow_dangerous_deserialization=True
    )

# if __name__ == "__main__":
#     from ingestion.loader import load_students
#     from ingestion.splitter import split_documents
#     from embeddings.embedder import get_embedding_model
#     documents = load_students("C:/Users/asus/Downloads/ANUJ_Student_Perfromance_RAG_Project/data/students.json")
#     split_docs = split_documents(documents)
#     embedding_model = get_embedding_model()
#     vectorstore = create_vector_store(split_docs, embedding_model)
#     save_vector_store(vectorstore)
#     loaded_vectorstore = load_vector_store(embedding_model)
#     print(loaded_vectorstore)

