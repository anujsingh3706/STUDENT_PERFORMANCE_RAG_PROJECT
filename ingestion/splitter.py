from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    return splitter.split_documents(documents)

if __name__ == "__main__":
    from ingestion.loader import load_students
    documents = load_students("C:/Users/asus/Downloads/ANUJ_Student_Perfromance_RAG_Project/data/students.json")
    split_docs = split_documents(documents)
    for doc in split_docs:
        print(doc.page_content)
        print(doc.metadata)

        print(len(split_docs))
        print("\n---\n")
