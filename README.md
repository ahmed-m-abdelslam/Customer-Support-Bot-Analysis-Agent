# Customer Support Bot Analysis Agent 🤖

An **Agentic AI system** for analyzing customer support conversations using **CrewAI**, **OpenAI**, and **FastAPI**.

The system processes raw customer chats and produces structured insights such as **intent**, **sentiment**, **urgency**, and a **final response**, following a multi-agent workflow.

---

## 🔹 Key Features
- Multi-agent architecture (Parser, Context Builder, Intent, Sentiment, Decision, Response)
- CrewAI for agent orchestration
- FastAPI backend with REST endpoint
- Simple frontend UI for testing
- JSON-based outputs for easy inspection

---

## 🧠 Agent Workflow
1. **Conversation Parser** – Converts raw chat into structured turns  
2. **Context Builder** – Builds conversation summary and statistics  
3. **Intent Detection** – Identifies the main customer intent  
4. **Sentiment & Urgency Analysis** – Detects customer emotion and urgency  
5. **Decision Agent** – Chooses the next action  
6. **Response Agent** – Generates a friendly final reply  

---

## 🛠 Tech Stack
- Python
- CrewAI
- OpenAI API
- FastAPI
- Pydantic
- HTML / JavaScript (Frontend)

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```
### 2. Run the backend
```bash
uvicorn main:app --reload

```
### 3. Run the frontend
```bash
cd src/frontend
python -m http.server 5500
open : http://127.0.0.1:5500

```

## 👤 Author
Ahmed
AI Engineer | Agentic AI & LLM Systems