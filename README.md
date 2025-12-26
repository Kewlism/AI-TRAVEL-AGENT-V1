✈️ AI Travel Agent Command Center

An autonomous, multi-agent system that plans, budgets, and manages complex travel itineraries in real time.

Semester Project: Agentic AI & RAG Systems
Track: A — Practical Agent System
Instructor: Engr. Asima Sarwar

📖 Table of Contents

Project Overview

Key Features

System Architecture

Technology Stack

Agent Capabilities

Installation & Setup

Usage Guide

Evaluation & Benchmarking

Project Structure

Future Roadmap

📌 Project Overview

The AI Travel Agent Command Center is not a traditional chatbot. It is a fully functional Agentic AI system capable of performing real-world planning tasks such as research, scheduling, and budgeting through coordinated autonomous agents.

The system solves the problem of fragmented travel planning by orchestrating multiple AI agents that reason over user constraints and dynamically update plans.

A key highlight is its Human-in-the-Loop design:

Users can reject any itinerary item

The system reasons about the rejection

A context-aware alternative is autonomously generated

The itinerary and budget are updated instantly
This demonstrates advanced state management, reasoning loops, and agent autonomy.

✨ Key Features
🌍 Autonomous Trip Planning

Generates detailed day-by-day itineraries

Considers destination, duration, group size, and travel style
(Luxury, Budget, Adventure)

🤖 Multi-Agent Orchestration

Research Agent:
Finds attractions, cultural landmarks, restaurants, and hidden gems

Booking Agent:
Estimates realistic costs for hotels, flights, and activities

🔄 Dynamic Self-Correction (“Swap Engine”)

Users can reject any itinerary item

The agent analyzes why it was rejected

A relevant alternative is swapped in without regenerating the entire trip

💰 Real-Time Budgeting

Live financial model

Automatically recalculates total cost when items change

⚡ Low-Latency Architecture

Powered by Groq LPU inference

Uses Llama-3.3-70B-Versatile

Average response time: < 3 seconds

🏗 System Architecture

The system follows a Client–Server architecture with a decoupled Agentic Brain.

🎨 Frontend — Command Center

HTML5, CSS3 (Glassmorphism), Vanilla JavaScript

Captures user intent

Renders structured agent outputs

Handles asynchronous UI updates (budget, swaps, timeline)

🔌 Backend — API Layer

FastAPI for high-performance APIs

Endpoints:

/start_plan — Initial itinerary generation

/replace_activity — Human-in-the-loop refinement

Pydantic schema validation ensures strict JSON compliance

🧠 Agent Layer — The Brain

LangChain Core for agent logic and prompt execution

Groq API for ultra-fast inference

Reasoning Loop:

Receive user constraints (state)

Reason about optimal plan

Generate structured JSON

Await user feedback

Refine state dynamically

🛠 Technology Stack
Category	Technology
Language	Python 3.10+
Backend Framework	FastAPI
AI Orchestration	LangChain Core, LangChain Groq
LLM	llama-3.3-70b-versatile
Frontend	HTML, CSS, Vanilla JS
Templating	Jinja2
Testing	Custom Python Benchmark Script
Deployment Ready	Yes
🧠 Agent Capabilities

This project fully satisfies Track-A requirements:

✅ Structured Reasoning

Agent outputs strict JSON only

No unstructured text

Guaranteed frontend compatibility

✅ Context Retention

Activity swaps respect:

Day

Location

Nearby activities

Prevents illogical replacements

✅ Tool Simulation

Simulated parallel sub-agents:

Research Agent

Booking Agent

Demonstrates realistic agent collaboration

🚀 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-travel-agent.git
cd ai-travel-agent

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file:

GROQ_API_KEY=your_api_key_here


Get a free API key from: https://console.groq.com

▶️ Usage Guide
Run the Application
python main.py

Access the Dashboard

Open your browser at:

http://localhost:8000

📊 Evaluation & Benchmarking

The project includes a custom automated evaluation pipeline as required.

Run Benchmark Tests
python evaluate.py

Metrics Assessed

Schema Compliance — Valid JSON generation

Constraint Satisfaction — Correct days & locations

Latency — Target < 3 seconds

Sample Output
DESTINATION | STATUS | LATENCY (s) | SCORE
------------------------------------------
Paris       | PASS   | 2.15        | 100/100
Tokyo       | PASS   | 2.80        | 100/100

Average Score: 100%
Average Latency: 2.3s

📂 Project Structure
/ai-travel-agent
│
├── main.py          # 🧠 FastAPI server & agent logic
├── evaluate.py      # 🧪 Automated benchmarking pipeline
├── requirements.txt # 📦 Dependencies
├── .env             # 🔑 API keys (not committed)
├── README.md        # 📄 Documentation
│
└── templates
    └── index.html   # 🎨 Frontend dashboard

🛣 Future Roadmap

🌐 Real-time flight & hotel APIs

🧭 Map-based itinerary visualization

💾 Persistent memory per user

🧑‍🤝‍🧑 Multi-user collaborative planning

☁️ Cloud deployment (AWS / GCP)
