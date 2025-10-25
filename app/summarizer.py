"""
summarizer.py
-------------
Takes raw search results and summarizes them using a Hugging Face model.
"""

import os
from huggingface_hub import InferenceClient

# ⚙️ Load your Hugging Face API token from environment variable
# (Make sure to set it in .env or terminal)
HF_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

# Initialize client
client = InferenceClient(token=HF_TOKEN)

# ✅ You can try other models too:
# "facebook/bart-large-cnn" (good summarizer)
# "google/flan-t5-base" (instruction-tuned)
# "tiiuae/falcon-7b-instruct" (strong generalist)
MODEL_NAME = "facebook/bart-large-cnn"


def generate_summary(topic: str, search_results: list[str]) -> str:
    """
    Combines fetched web results into a single context and summarizes them.

    Args:
        topic (str): The topic to summarize.
        search_results (list[str]): List of text snippets or paragraphs from the web.

    Returns:
        str: AI-generated summary of the topic.
    """
    try:
        # Combine the top few results into one big context
        combined_text = " ".join(search_results[:5])

        # Create a task prompt
        prompt = f"""
        Summarize the following information about '{topic}' in 3–5 bullet points:

        {combined_text}

        Summary:
        """

        # Send to HF inference endpoint
        response = client.summarization(combined_text,model="facebook/bart-large-cnn")
        if not response:
            return "Summary could not be generated. Try a different topic or model."

        return response

    except Exception as e:
        print(f"[ERROR in generate_summary]: {e}")
        return "Summary could not be generated."
