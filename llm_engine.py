"""
This module integrates the language model for the chatbot.
It uses the Google Generative AI model to generate responses based on a user's
query and the retrieved context. It also manages the conversation history
to support multi-turn conversations.

The module performs the following steps:
1. Initializes the ChatGoogleGenerativeAI model.
2. Creates a conversational retrieval chain that combines the retriever,
   the language model, and conversation history.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from retriever import get_retriever
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Google API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def get_llm_engine():
    """
    Creates and returns a conversational retrieval chain.

    Returns:
        chain: A conversational retrieval chain object.
    """
    # Initialize the language model
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY,
                                 temperature=0.7, convert_system_message_to_human=True)

    # Initialize the conversation memory
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # Get the retriever
    retriever = get_retriever()

    # Create the conversational retrieval chain
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory
    )

    return chain

if __name__ == "__main__":
    # This block is for testing the LLM engine functionality independently
    chain = get_llm_engine()
    # Example usage:
    # response = chain({"question": "What is your return policy?"})
    # print(response)
    print("LLM engine created successfully.")
