# modules/ai_module.py
import os
import certifi
import openai
import ssl

# Ensure the requests library uses the certifi certificate bundle
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()

# OPTIONAL: Disable SSL verification (for debugging only, not for production)
# ssl._create_default_https_context = ssl._create_unverified_context

def initialize_openai(api_key: str):
    """
    Initialize the OpenAI API by setting the API key.
    """
    openai.api_key = api_key

def generate_insight_report(data, report_type: str, user_query: str) -> str:
    """
    Generate an insight report by sending a prompt to the OpenAI ChatCompletion API.
    
    Aggregates a summary from the NC/CAPA data and includes the user's query in a conversation-style prompt.
    """
    total_nc = len(data)
    departments = data["Department"].nunique() if "Department" in data.columns else "N/A"
    open_capa = data[data["Status"] == "Open"].shape[0] if "Status" in data.columns else "N/A"

    summary = (
        f"NC/CAPA Data Summary:\n"
        f"- Total nonconformance records: {total_nc}\n"
        f"- Number of departments involved: {departments}\n"
        f"- Number of open CAPA actions: {open_capa}\n"
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are a quality management data analyst. Your task is to analyze NC/CAPA data and provide an "
                "in-depth report with actionable insights and recommendations. The report should identify trends, "
                "potential root causes, and suggest corrective and preventive actions."
            )
        },
        {
            "role": "user",
            "content": (
                f"Given the following summary:\n{summary}\n"
                f"User Query: {user_query}\n"
                "Generate a detailed report that identifies trends and offers actionable recommendations."
            )
        }
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=1024,
            temperature=0.5
        )
        report = response.choices[0].message["content"].strip()
        return report
    except Exception as e:
        return f"Error generating report: {e}"
