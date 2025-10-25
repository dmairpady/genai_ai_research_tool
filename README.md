🧠 AI Research Assistant — FastAPI + Hugging Face
An open-source AI agent that searches the web and writes concise research summaries using open-weight LLMs.

📘 Overview

The AI Research Assistant is a mini-RAG (Retrieval + Generation) system that:
1️⃣ Accepts a topic or question.
2️⃣ Searches the web for factual sources.
3️⃣ Generates a summarized research report using a Hugging Face model.

This demonstrates how to combine FastAPI, search APIs, and LLMs into a production-style Generative AI backend.

⚙️ Tech Stack
Layer	Tool / Library	Purpose
🧠 LLM	google/flan-t5-base or tiiuae/falcon-7b-instruct	Text summarization / generation
⚙️ Backend	FastAPI	REST API service
🔍 Retrieval	DuckDuckGo / Serper API	Web search
☁️ Hosting	Render / Hugging Face Spaces / Docker	Deployment
🧪 Testing	Pytest (optional)	Unit testing endpoints
🧩 Architecture
User → FastAPI Endpoint (/generate_report)
        ├─► search_engine.py → fetch_search_results()
        ├─► summarizer.py → generate_summary()
        └─► Return JSON { topic, sources, summary }

🚀 Quick Start
1️⃣ Clone the repo
git clone https://github.com/<yourusername>/ai-research-assistant.git
cd ai-research-assistant/app

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add environment variables

Create .env file:

HF_TOKEN=your_huggingface_token
SEARCH_API_KEY=your_search_api_key

4️⃣ Run locally
uvicorn main:app --reload


Visit 👉 http://127.0.0.1:8000/docs
 for the interactive Swagger UI.

🧠 Example Request

Endpoint:

POST /generate_report


Body:

{
  "topic": "AI in Healthcare"
}


Response:

	
Response body
Download
{
  "status": "Report generated",
  "topic": "AI in healthcare",
  "sources": [
    "Artificial intelligence in healthcare is the application of artificial intelligence (AI) to analyze and understand complex medical and healthcare data. In some cases, it can exceed or augment human capabilities by providing better or faster ways to diagnose, treat, or prevent disease.As the widespread use of artificial intelligence in healthcare is still relatively new, research is ongoing into its applications across various medical subdisciplines and related industries. AI programs are being applied to practices such as diagnostics, treatment protocol development, drug development, personalized medicine, and patient monitoring and care. Since radiographs are the most commonly performed imaging tests in radiology, the potential for AI to assist with triage and interpretation of radiographs is particularly significant.Using AI in healthcare presents unprecedented ethical concerns related to issues such as data privacy, automation of jobs, and amplifying already existing algorithmic bias. New technologies such as AI are often met with resistance by healthcare leaders, leading to slow and erratic adoption. There have been cases where AI has been put to use in healthcare without proper testing. A systematic review and thematic analysis in 2023 showed that most stakeholders including health professionals, patients, and the general public doubted that care involving AI could be empathetic. Meta-studies have found that the scientific literature on AI in healthcare often suffers from a lack of reproducibility.",
    "Aug 13, 2025 · While healthcare lags in AI adoption, these game-changing innovations - from spotting broken bones to assessing ambulance needs - show what's possible.",
    "Jan 7, 2020 · By 2030, AI will access multiple sources of data to reveal patterns in disease and aid treatment and care. Healthcare systems will be able to predict an individual's risk of certain …"
  ],
  "summary": {
    "summary_text": "Artificial intelligence in healthcare is the application of artificial intelligence to analyze and understand complex medical and healthcare data. In some cases, it can exceed or augment human capabilities by providing better or faster ways to diagnose, treat, or prevent disease. Using AI in healthcare presents unprecedented ethical concerns related to issues such as data privacy, automation of jobs, and amplifying already existing algorithmic bias."
  }
}

🐳 Docker Deployment

Dockerfile

FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]


Build & Run

docker build -t ai-research-assistant .
docker run -p 8080:8080 ai-research-assistant

📸 Demo Screenshot

(Add one from Swagger UI here)


🧰 Folder Structure
ai-research-assistant/
│
├── app/
│   ├── main.py             # FastAPI entry point
│   ├── search_engine.py    # web search logic
│   ├── summarizer.py       # Hugging Face LLM logic
│   ├── requirements.txt
│   ├── .env.example
│
├── tests/
│   └── test_app.py
│
├── README.md
└── screenshots/
    └── demo_ui.png

🔍 Future Improvements

✅ Streamlit front-end for interactive UI

✅ Add citation references per sentence

✅ Multi-model switcher (select model at runtime)

✅ Integration with local embeddings (Chroma/FAISS)