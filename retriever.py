"""
This module provides the retrieval functionality for the chatbot.
It loads a pre-built FAISS vector store and retrieves the most relevant
document chunks based on a user's query.

The module performs the following steps:
1. Initializes the GoogleGenerativeAIEmbeddings model.
2. Loads the FAISS vector store from the local 'faiss_index' directory.
3. Creates a retriever from the FAISS vector store to find relevant documents.
"""

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Google API key from environment variables
GOOGLE_API_key = os.getenv("GOOGLE_API_KEY")

# Initialize the embeddings model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_key)

def get_retriever():
    """
    Creates and returns a retriever for the FAISS vector store.

    Returns:
        retriever: A retriever object for the FAISS vector store.
    """
    # Load the FAISS vector store from the local directory
    db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

    # Create a retriever from the FAISS vector store
    retriever = db.as_retriever(search_kwargs={"k": 5})
    return retriever

if __name__ == "__main__":
    # This block is for testing the retriever functionality independently
    retriever = get_retriever()
    # Example usage:
    # results = retriever.get_relevant_documents("What is your return policy?")
    # print(results)
    print("Retriever created successfully.")
