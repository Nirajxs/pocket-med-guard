## AI Health Misinformation Detection App (FastAPI + Frontend)
<p align="center">


</p>

<h1 align="center">🛡️ AI Health Misinformation Guard</h1>
<p align="center">FastAPI + Frontend Project</p>

---

## 🧠 Project Summary

Pocket Med Guard is an AI-powered health misinformation detection system designed to identify whether medical information shared online is accurate, misleading, or fake. The project uses a FastAPI backend to process text inputs and an intelligent machine learning model to analyze the reliability of the content. A clean, simple frontend interface allows users to enter any medical claim or statement, which the AI evaluates and returns a factual, trustworthy assessment. This tool aims to help students, patients, and general users avoid harmful misinformation by providing quick, reliable, and evidence-based verification of health-related content.

- ✔ Accurate  
- ⚠️ Misleading  
- ❌ Fake / Harmful  



---

## 🚀 Features

- 🧠 AI-based medical misinformation detection  
- ⚡ FastAPI backend  
- 🎨 Clean & simple frontend UI  
- 📡 Real-time response  
- 📁 Lightweight project structure  
- 🔧 Easy integration & deployment  



Pocket Med Guard is an AI-powered health misinformation detection system that analyzes medical content and determines whether the information is accurate, misleading, or fake.
<br>

<strong>⭐ Project Workflow in Both Explation and flowchart</strong>  —<hr>

  1️⃣ User Input (Frontend Chat UI)

The user opens the frontend at:
/app/frontend/index.html

A chat-style UI allows the user to type any medical claim, question, or statement.

The message is sent to the backend API route:
POST → /message
<br>

2️⃣ API Request Handling (FastAPI Backend)

The incoming user message is received by FastAPI.

It triggers the conversation pipeline through the agent implemented in agents.py.

CORS is enabled so frontend ↔ backend communication works smoothly.
<br>



3️⃣ Claim Parsing & Keyword Extraction

Modules used:

claim_parser.py

verifier.py

Steps:

The system cleans & structures the text.

Medical keywords are extracted using a custom medical keyword bank.

Parsed claim is prepared for evidence lookup.

This is the first layer of verifying what the user is actually claiming.

<br>



4️⃣ Evidence Retrieval from Offline CSV Files

Module: evidence_fetcher.py
Data files:

claims_train.csv

claims_test.csv

Process:

The system searches for relevant records inside offline medical datasets.

Evidence entries related to the detected keywords are fetched.

Each piece of evidence is assigned a similarity score or relevance score.

This ensures the AI does not guess but relies on factual data.
<br>

5️⃣ Evidence Scoring & Verdict Generation

Module: verifier.py

All evidence is scored using:
✔ keyword match intensity
✔ claim similarity
✔ pre-existing dataset labels

The system evaluates whether the claim is:

Accurate

Misleading

Fake / Unsupported

The verdict logic has been improved to produce medically aware decisions.

<br>

6️⃣ Human-Like Response Generation (Conversation Agent)

Module: agents.py (ConversationAgent)

The agent takes:

Parsed claim

Evidence scores

Final verdict

It generates a human-like medical explanation instead of a robotic answer.

The explanation includes:
✔ Reasoning
✔ Supporting facts
✔ Simple medical interpretation

This improves user experience and clarity.
<br>

7️⃣ Memory Storage (JSON Memory)

Module: memory.py

Every interaction (user message + system response) is stored in JSON format.

This allows the agent to maintain conversation context.

Helpful for multi-turn conversations and follow-up questions.

<br>
8️⃣ Logging & Monitoring

Module: logging_config.py

Every request, response, error, and evidence result is logged.

Helps debugging, accuracy improvements, and analytics.

<br>
9️⃣ Response Sent Back to Frontend

FastAPI returns a JSON response:

{
   "response": "...",
   "verdict": "accurate/misleading/fake",
   "keywords": [...],
   "evidence_used": [...]
}


The UI displays:
✔ Human-like medical answer
✔ Verdict badge
✔ Neat chat bubble animation
<br>

🔟 Frontend Display & User Interaction

Chat bubbles show user queries & agent replies.

Smooth scrolling, typing effect, and message UI.

Users can continue chatting → pipeline repeats from Step 1.

<br><strong> Here Flowchart</strong><hr>
                   ┌──────────────────────────┐
                   │      User Interaction     │
                   │  (Frontend Chat UI opens) │
                   └───────────────┬───────────┘
                                   │
                                   ▼
                      ┌────────────────────────┐
                      │  User enters medical   │
                      │    claim/question      │
                      └─────────────┬──────────┘
                                    │
                                    ▼
                     ┌──────────────────────────┐
                     │ Frontend sends message   │
                     │   → POST /message        │
                     └──────────────┬───────────┘
                                     │
                                     ▼
               ┌────────────────────────────────────────┐
               │     FastAPI Backend Receives Input     │
               │   (Request handled by ConversationAgent)│
               └────────────────┬────────────────────────┘
                                │
                                ▼
                  ┌────────────────────────────┐
                  │  Claim Parsing Begins      │
                  │ (claim_parser.py)          │
                  │ - Text cleaning            │
                  │ - Keyword extraction       │
                  └───────────────┬────────────┘
                                  │
                                  ▼
                ┌────────────────────────────────┐
                │ Evidence Fetching (CSV files)  │
                │ evidence_fetcher.py            │
                │ - claims_train.csv             │
                │ - claims_test.csv              │
                └─────────────────┬──────────────┘
                                  │
                                  ▼
              ┌───────────────────────────────────────┐
              │ Evidence Scoring & Similarity Check   │
              │ verifier.py                           │
              │ - Keyword match                       │
              │ - Dataset labels                      │
              │ - Verdict calculation                 │
              └──────────────────┬────────────────────┘
                                 │
                                 ▼
                     ┌─────────────────────────────┐
                     │ Generate Human-like Response │
                     │ agents.py                    │
                     │ - Verdict → Accurate /       │
                     │   Misleading / Fake          │
                     │ - Explanation text           │
                     └───────────────┬─────────────┘
                                     │
                                     ▼
                   ┌──────────────────────────────────┐
                   │   Save Conversation to Memory    │
                   │         (JSON memory)            │
                   │        memory.py                 │
                   └────────────────┬─────────────────┘
                                    │
                                    ▼
               ┌────────────────────────────────────────┐
               │   Backend Returns JSON Response        │
               │  (response + verdict + evidence used)  │
               └────────────────────┬───────────────────┘
                                    │
                                    ▼
                    ┌────────────────────────────────┐
                    │ Frontend displays response     │
                    │ - Chat bubbles                 │
                    │ - Verdict badge                │
                    │ - Typing animation             │
                    └────────────────────────────────┘


<hr>
<b>This is steps to Run the project </b><br>
          ┌──────────────────────────────┐
          │ 1. Open VS Code              │
          └───────────────┬──────────────┘
                          │
                          ▼
         ┌─────────────────────────────────┐
         │ 2. Create Virtual Environment   │
         │    python -m venv venv          │
         └────────────────┬────────────────┘
                          │
                          ▼
      ┌─────────────────────────────────────────┐
      │ 3. Activate Venv                        │
      │    Windows: .\venv\Scripts\activate     │
      │    Linux/Mac: source venv/bin/activate  │
      └──────────────────┬──────────────────────┘
                         │
                         ▼
      ┌─────────────────────────────────────────┐
      │ 4. Install Dependencies                 │
      │    pip install -r requirements.txt      │
      └──────────────────┬──────────────────────┘
                         │
                         ▼
        ┌────────────────────────────────────┐
        │ 5. Run FastAPI Server               │
        │    uvicorn main:app --reload        │
        └───────────────────┬─────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────┐
        │ 6. Open Frontend (Chat UI)        │
        │    http://127.0.0.1:8000          │
        └───────────────────────────────────┘


<hr>
##  🚀 project structure 
pocket-med-guard/
│── frontend/
│── backend/
│── static/
│── templates/
│── main.py
│── requirements.txt
│── README.md


## 🏗️ Tech Stack

| Layer | Technology |
|------|------------|
| Backend | FastAPI, Python |
| Frontend | HTML, CSS, JavaScript |
| AI/ML | Custom Model (Add your model name) |
| Deployment | Localhost / Cloud |

---
<hr>
## STEPS TO RUN THIS PROJECT

<img width="1024" height="1024" alt="ai health" src="https://github.com/user-attachments/assets/04426586-04a9-472b-8d97-ec4d81c42bbc" /><hr>
<img width="1024" height="1024" alt="ai" src="https://github.com/user-attachments/assets/5c07f330-cc98-473e-82c6-29d969189489" />


## 📦 Installation & Setup

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Nirajxs/pocket-med-guard
cd pocket-med-guard


📜 License

This project is licensed under the MIT License.<img width="1024" height="1024" alt="ChatGPT Image Nov 28, 2025, 10_39_15 PM" src="https://github.com/user-attachments/assets/5f376cf1-a164-4eb1-b9d0-0752b8d841c6" />


👤 Author

Niraj Kumar
AI Health Systems Developer
Pocket Med Guard – 2025
