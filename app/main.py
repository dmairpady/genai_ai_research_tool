"""
AI Research Assistant 🧠
-----------------------
FastAPI app that:
1. Accepts a topic from user
2. Fetches web search results
3. Summarizes the information using a Hugging Face model

Author: Your Name
GitHub: https://github.com/<yourusername>/ai-research-assistant
"""

from fastapi import FastAPI
from pydantic import BaseModel
from search_engine import fetch_search_results
from summarizer import generate_summary

app = FastAPI(
    title="AI Research Assistant",
    description="An AI-powered tool that searches the web and summarizes insights on any topic.",
    version="1.0.0"
)


class Query(BaseModel):
    topic: str


@app.post("/generate_report")
async def create_report(query: Query):
    """
    Accepts a topic, performs a web search, and returns a summarized report.
    """
    try:
        # Step 1: Get search results
        search_results = fetch_search_results(query.topic)
        if not search_results:
            return {"error": "No relevant information found."}

        # Step 2: Generate summary from search content
        summary = generate_summary(query.topic, search_results)

        # Step 3: Return structured report
        return {
            "status": "Report generated successfully ✅",
            "topic": query.topic,
            "sources": search_results,
            "summary": summary,
        }

    except Exception as e:
        return {"error": f"Something went wrong: {str(e)}"}


@app.get("/")
async def root():
    return {
        "message": "Welcome to the AI Research Assistant API! 🚀",
        "usage": "POST a JSON body to /generate_report with { 'topic': 'your topic' }"
    }
