# modules/ui_module.py
import streamlit as st

def get_api_key() -> str:
    """
    Display a text input in the sidebar for the user to enter their OpenAI API key.
    """
    return st.sidebar.text_input("Enter your OpenAI API key", type="password")
