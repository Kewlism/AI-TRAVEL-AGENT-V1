✈️ AI Travel Agent Command Center
An autonomous, multi-agent system that plans, budgets, and manages complex travel itineraries in real-time.

Semester Project: Agentic AI & RAG Systems (Track A)

Instructor: Engr. Asima Sarwar * Track: A - Practical Agent System 
+1

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
The AI Travel Agent Command Center is not just a chatbot; it is a fully functional Agentic System capable of performing real-world planning actions. It solves the problem of fragmented travel planning by orchestrating multiple AI agents to handle research, scheduling, and budgeting simultaneously.

The system features a "Human-in-the-Loop" design. Users don't just receive a static plan; they interact with it. If a user rejects an activity, the agent dynamically reasons about the rejection, searches for a context-aware alternative, and updates the entire itinerary and budget model instantly—demonstrating sophisticated state management and reasoning loops.

✨ Key Features
🌍 Autonomous Trip Planning: Generates day-by-day itineraries based on destination, duration, group size, and travel style (Luxury, Budget, Adventure).

🤖 Multi-Agent Orchestration:

Research Agent: Scours knowledge bases to find hidden gems, top-rated restaurants, and cultural landmarks.

Booking Agent: Estimates real-time costs for hotels, flights, and activities to build a realistic financial model.

🔄 Dynamic Self-Correction (The "Swap" Engine): Users can reject any item in the itinerary. The agent analyzes the rejection and autonomously swaps it for a relevant alternative without regenerating the entire trip.

💰 Real-Time Budgeting: A live financial engine that recalculates the total trip cost instantly whenever an activity is added, removed, or swapped.

⚡ Low-Latency Architecture: Powered by Groq's LPU inference engine running Llama-3.3-70b-versatile, achieving sub-3-second response times for complex planning tasks.

🏗 System Architecture
The project follows a Client-Server Architecture with a decoupled Agentic Brain.

Frontend (The Command Center):

Built with HTML5, CSS3 (Glassmorphism), and JavaScript.

Acts as the "Action Layer," capturing user intent and rendering agent outputs.

Handles asynchronous state updates (Budget recalculation, DOM manipulation).

Backend (The API Layer):

FastAPI serves as the bridge between the UI and the AI.

Exposes endpoints /start_plan (initial generation) and /replace_activity (refinement loop).

Enforces strict JSON schema validation using Pydantic models.

The "Brain" (Agent Layer):

LangChain handles prompt engineering and chain execution.

Groq API provides the inference power.

Reasoning Loop: The agent receives a state (User Constraints), reasons about the best course of action, generates structured data, and awaits feedback.

🛠 Technology Stack
Language: Python 3.10+

Framework: FastAPI (Backend), Jinja2 (Templating)

AI Orchestration: LangChain Core, LangChain Groq

LLM Model: llama-3.3-70b-versatile (State-of-the-Art open source model)

Frontend: Vanilla JS, CSS Variables, Fetch API

Testing: Custom Python Benchmarking Script (requests, statistics)

🧠 Agent Capabilities
This system fulfills the Track A requirements by implementing:

Structured Reasoning: The agent does not output unstructured text. It strictly adheres to a complex JSON schema, ensuring data interoperability with the frontend.

Context Retention: When swapping an activity, the agent retains the context of the trip (e.g., "If the user is in Tokyo on Day 2, finding a replacement activity must be geographically close to other Day 2 activities").

Tool Simulation: The system simulates two distinct sub-agents (Research & Booking) that run in parallel to populate the dashboard.

🚀 Installation & Setup
Follow these steps to deploy the agent locally.

1. Clone the Repository
2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.
3. Install Dependencies
4. Configure Environment Variables
Create a .env file in the root directory and add your Groq API key (free tier available at console.groq.com).

📊 Evaluation & Benchmarking
Per the project requirements, the agent includes a custom automated evaluation pipeline.

Running the Benchmark
To test the agent's performance, stability, and speed, run the evaluation script:
python evaluate.py

Metrics Assessed
The script tests the agent against a "Golden Dataset" of 5 diverse scenarios (e.g., Luxury Trip to Paris vs. Budget Trip to Tokyo) and measures:

Schema Compliance: Success rate of generating valid, parseable JSON.

Constraint Satisfaction: Accuracy in respecting user inputs (Days, Location).

Latency: Response time (Target: <3.0 seconds).

Sample Output:
DESTINATION     | STATUS     | LATENCY (s)  | SCORE     
------------------------------------------------------------
Paris           | PASS       | 2.15         | 100/100
Tokyo           | PASS       | 2.80         | 100/100
...
Average Score: 100%
Average Latency: 2.3s

📂 Project Structure
/ai-travel-agent
│
├── main.py                 # 🧠 The Brain: FastAPI Server & Agent Logic
├── evaluate.py             # 🧪 The Test: Automated Benchmarking Pipeline
├── requirements.txt        # 📦 Dependencies
├── .env                    # 🔑 Secrets (API Keys - Not committed)
├── README.md               # 📄 Documentation
│
└── templates
    └── index.html          # 🎨 The Face: Frontend Dashboard (HTML/JS/CSS)
