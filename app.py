"""
This is the main application file for the Streamlit chatbot UI.
It integrates the other modules to create a functional chatbot.

The application performs the following steps:
1. Sets up the Streamlit page configuration.
2. Initializes the LLM engine.
3. Manages the chat history in the Streamlit session state.
4. Displays the chat history.
5. Accepts user input and gets the chatbot's response.
6. Displays the chatbot's response and the sources used.
"""

import streamlit as st
from llm_engine import get_llm_engine

def main():
    """
    Main function to run the Streamlit chatbot application.
    """
    # Set up the Streamlit page
    st.set_page_config(page_title="AI Customer Support Chatbot", page_icon="🤖")
    st.title("🤖 AI Customer Support Chatbot")
    st.write("Welcome! Ask me anything about our products, shipping, or returns.")

    # Initialize the LLM engine
    chain = get_llm_engine()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is your question?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get the chatbot's response
        with st.spinner("Thinking..."):
            response = chain({"question": prompt})
            answer = response["answer"]
            sources = set([doc.metadata["source"] for doc in response["source_documents"]])

        # Display chatbot response in chat message container
        with st.chat_message("assistant"):
            st.markdown(answer)
            if sources:
                st.write("Sources:")
                for source in sources:
                    st.write(f"- {source}")

        # Add chatbot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    main()
