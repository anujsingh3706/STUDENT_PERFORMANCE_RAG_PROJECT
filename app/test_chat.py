from rag.chain import RAGChatbot

def main():
    bot = RAGChatbot()

    print("🎓 Student RAG Chatbot (type 'exit' to quit)\n")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            break

        response = bot.chat(query)
        print("\nBot:", response, "\n")


if __name__ == "__main__":
    main()