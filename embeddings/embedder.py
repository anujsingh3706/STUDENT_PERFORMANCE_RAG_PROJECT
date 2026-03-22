from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():
    model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return model

# if __name__ == "__main__":
#     embedding_model = get_embedding_model()
#     print(embedding_model)
