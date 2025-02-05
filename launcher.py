# launcher.py
import subprocess
import time
import webview
import threading
import sys

def start_streamlit():
    """
    Start the Streamlit app in a separate process.
    """
    # Launch Streamlit using the current Python interpreter.
    # Adjust the command if necessary (e.g., if using a virtualenv).
    process = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "finalapp.py"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    return process

def create_window():
    """
    Create a native window using PyWebView pointing to the Streamlit app.
    """
    # Use the URL where Streamlit is running (default is localhost:8501).
    webview.create_window("NC/CAPA Insight Reviewer", "http://localhost:8501", width=1200, height=800)
    webview.start()

if __name__ == '__main__':
    # Start Streamlit in a background process.
    streamlit_process = start_streamlit()
    
    # Wait for a few seconds to let the Streamlit server start up.
    time.sleep(5)
    
    try:
        create_window()
    finally:
        # When the window is closed, terminate the Streamlit process.
        streamlit_process.terminate()
