# modules/ai_module.py
import openai

def initialize_openai(api_key: str):
    """
    Initialize the OpenAI API by setting the API key.
    """
    openai.api_key = api_key

def generate_insight_report(data, report_type: str, user_query: str) -> str:
    """
    Generate an insight report by sending a prompt to the OpenAI ChatCompletion API.
    
    It aggregates a summary from the provided NC/CAPA data and includes the user's query
    in a conversation-style prompt.
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

    # Construct the conversation messages:
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
        # Use the new ChatCompletion.create interface
        response = openai.Completion.create(
            model="gpt-4",
            messages=messages,
            max_tokens=1024,
            temperature=0.5
        )
        # Extract the generated text from the response
        report = response.choices[0].message["content"].strip()
        return report
    except Exception as e:
        return f"Error generating report: {e}"
