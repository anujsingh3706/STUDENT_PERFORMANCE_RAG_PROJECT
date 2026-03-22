from ingestion.loader import load_students
from ingestion.splitter import split_documents
from embeddings.embedder import get_embedding_model
from vectorstore.vectordb import create_vector_store, save_vector_store

DATA_PATH = "data/students.json"

def main():
    print("📥 Loading data...")
    documents = load_students(DATA_PATH)

    print("✂️ Splitting documents...")
    chunks = split_documents(documents)

    print("🔎 Creating embeddings...")
    embedding_model = get_embedding_model()

    print("📦 Creating vector store...")
    vectorstore = create_vector_store(chunks, embedding_model)

    print("💾 Saving index...")
    save_vector_store(vectorstore)

    print("✅ Index built successfully!")

if __name__ == "__main__":
    main()