# modules/chat_module.py
import openai
import streamlit as st

def init_chat():
    """
    Initialize chat history in session state if it doesn't already exist.
    """
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def send_chat_message(user_message: str) -> str:
    """
    Append the user's message to the conversation, send the updated conversation to the OpenAI API,
    and return the assistant's reply.
    """
    st.session_state.chat_history.append({"role": "user", "content": user_message})
    
    # Define the system message (included at the beginning of the conversation)
    system_message = {
        "role": "system",
        "content": (
            "You are a quality management data analyst. Engage in a helpful and iterative conversation with the user "
            "to refine and improve insights based on NC/CAPA data."
        )
    }
    
    # Construct messages for the API: system message followed by the conversation history
    messages = [system_message] + st.session_state.chat_history

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=512,
            temperature=0.5
        )
        assistant_reply = response.choices[0].message["content"].strip()
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_reply})
        return assistant_reply
    except Exception as e:
        return f"Error communicating with OpenAI: {e}"
