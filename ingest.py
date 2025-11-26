"""
This script ingests text documents from a specified directory, splits them into chunks,
generates embeddings for each chunk using a pre-trained model, and stores the embeddings
in a FAISS vector store for efficient retrieval.

The script performs the following steps:
1. Loads documents from the 'data/' directory using DirectoryLoader.
2. Splits the loaded documents into smaller chunks using RecursiveCharacterTextSplitter.
3. Initializes the GoogleGenerativeAIEmbeddings model for generating embeddings.
4. Creates a FAISS vector store from the document chunks and their embeddings.
5. Saves the FAISS vector store locally to 'faiss_index'.
"""

from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Google API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize the embeddings model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)

def main():
    """
    Main function to perform the ingestion process.
    """
    # Load documents from the 'data/' directory
    loader = DirectoryLoader('data/', glob="*.txt")
    documents = loader.load()

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    text_chunks = text_splitter.split_documents(documents)

    # Create FAISS vector store from the document chunks and embeddings
    db = FAISS.from_documents(text_chunks, embeddings)

    # Save the FAISS vector store locally
    db.save_local("faiss_index")
    print("Ingestion complete. FAISS index created and saved to 'faiss_index'.")

if __name__ == "__main__":
    main()
