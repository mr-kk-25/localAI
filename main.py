from langchain_ollama import OllamaLLMMore actions
from langchain_core.prompts import ChatPromptTemplate

# Corrected prompt template string
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Fixed typos in model name and class/method names
model = OllamaLLM(model="gemma")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        result = chain.invoke({"context": context, "question": user_input})
        print("Bot:", result)
        context += f"\nUser: {user_input}\nAI: {result}"

# Fixed the `if __name__ == "__main__"` syntax
if __name__ == "__main__":
    handle_conversation()