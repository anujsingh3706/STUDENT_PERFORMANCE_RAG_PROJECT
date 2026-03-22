from vectorstore.vectordb import load_vector_store
from embeddings.embedder import get_embedding_model
from rag.llm import GroqLLM
from memory.memory import get_memory

class RAGChatbot:
    def __init__(self):
        self.embedding_model = get_embedding_model()
        self.vectorstore = load_vector_store(self.embedding_model)
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 3})
        self.llm = GroqLLM()
        self.memory = get_memory()

    def generate_prompt(self, query, docs, chat_history):
        context = "\n\n".join([doc.page_content for doc in docs])

        history_text = ""
        for msg in chat_history:
            history_text += f"{msg}\n"

        prompt = f"""
        You are an AI assistant for student performance analysis.

        Chat History:
        {history_text}

        Context:
        {context}

        Question:
        {query}

        Answer in a helpful and structured way.
        """

        return prompt

    def chat(self, query: str):
        docs = self.retriever.get_relevant_documents(query)

        chat_history = self.memory.load_memory_variables({})["chat_history"]

        prompt = self.generate_prompt(query, docs, chat_history)

        response = self.llm.generate(prompt)

        self.memory.save_context(
            {"input": query},
            {"output": response}
        )

        return response