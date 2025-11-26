# 🤖 AI-Driven Customer Support Chatbot

A **context-aware customer support chatbot** powered by **Retrieval-Augmented Generation (RAG)** and **Google Gemini AI** to answer FAQs from a company knowledge base. This project provides a modular and scalable framework for building and deploying a customer support chatbot.

## 🚀 Features

-   **Ingests and embeds FAQ documents**: Processes text files from a `data` directory and stores them in a FAISS vector store for efficient retrieval.
-   **Retrieves most relevant chunks**: Based on a user's query, the chatbot retrieves the most relevant text chunks from the knowledge base.
-   **Generates conversational responses**: Uses Google Gemini AI to generate human-like responses based on the retrieved context.
-   **Multi-turn conversation with memory**: Remembers the context of the conversation to provide more relevant and accurate answers over multiple turns.
-   **Transparent results**: Shows the sources used to generate the answer, providing transparency and trust to the user.

## 🛠 Tech Stack

-   **Python**: The core programming language for the project.
-   **Streamlit**: Used to create the simple and interactive chat user interface.
-   **LangChain**: A framework for developing applications powered by language models.
-   **FAISS**: A library for efficient similarity search and clustering of dense vectors.
-   **Google Gemini AI**: The language model used for generating responses.
-   **Dotenv**: For managing environment variables.

## 📊 Business Value

-   **Automates FAQ responses**: This chatbot can automate a significant portion of frequently asked questions, freeing up human agents to handle more complex issues.
-   **Reduces support ticket resolution time**: By providing instant answers to common questions, the chatbot can significantly reduce the time it takes to resolve customer issues.
-   **Improves customer satisfaction**: Customers get instant support, which improves their overall experience with the brand.

### Dummy Calculation:

-   **60% of FAQs automated**: Based on an analysis of common support tickets, the chatbot can handle up to 60% of incoming queries.
-   **Saving 100 hours of agent time per month**: By automating these queries, the chatbot can save approximately 100 hours of human agent time per month, leading to significant cost savings.

## 🏗 Project Structure

```
support_chatbot/
├── data/
│   ├── products.txt
│   ├── returns.txt
│   └── shipping.txt
├── ingest.py
├── retriever.py
├── llm_engine.py
├── app.py
├── requirements.txt
└── README.md
```

## ▶️ How to Run

1.  **Clone this repo**:
    ```bash
    git clone https://github.com/yourusername/ai-support-chatbot
    ```
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up your environment variables**:
    Create a `.env` file in the root of the project and add your Google API key:
    ```
    GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
    ```
4.  **Run the ingestion script**:
    ```bash
    python ingest.py
    ```
5.  **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

## 📸 Demo

*(Insert screenshot of chatbot UI here)*

## Example Q&A

**Q:** How can I reset my password?
**A:** "Click on 'Forgot Password' on the login page and follow the steps. [Source: password_reset_guide.pdf]"

**Q:** What are your shipping options?
**A:** "We offer standard, expedited, and overnight shipping. Standard shipping takes 5-7 business days, expedited takes 2-3 business days, and overnight shipping arrives the next business day. [Source: data/shipping.txt]"