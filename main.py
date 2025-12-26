import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import json
import random

# 1. Load Keys
load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# 2. Setup Groq Model (Llama 3.3 for high intelligence)
llm = ChatGroq(
    temperature=0.4, # Slightly creative for alternatives
    model_name="llama-3.3-70b-versatile", 
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# 3. Data Models
class TripRequest(BaseModel):
    destination: str
    days: int
    travelers: int
    experience: str

class ReplaceRequest(BaseModel):
    destination: str
    old_activity: str
    experience: str

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/start_plan")
async def start_plan(trip: TripRequest):
    print(f"🤖 Agent starting job for: {trip.destination}")

    prompt = f"""
    You are an expert Travel Agent. Plan a {trip.days}-day trip to {trip.destination} for {trip.travelers} people.
    Style: {trip.experience}.

    Return strictly valid JSON. No markdown. Structure:
    {{
        "trip_details": {{
            "destination": "{trip.destination}",
            "days": {trip.days},
            "travelers": {trip.travelers},
            "experience": "{trip.experience}",
            "title": "A catchy title"
        }},
        "research_findings": [
            {{ "name": "Attraction", "type": "Type", "match_score": 95 }}
        ],
        "booking_options": [
            {{ "name": "Hotel Name", "category": "Accommodation", "cost": 400 }},
            {{ "name": "Flight Estimate", "category": "Transport", "cost": 600 }}
        ],
        "itinerary": [
            {{
                "day": 1,
                "theme": "Theme",
                "activities": [
                    {{ "time": "09:00 AM", "activity": "Activity Name", "description": "Short details", "cost": 20 }},
                    {{ "time": "01:00 PM", "activity": "Lunch", "description": "Food details", "cost": 50 }}
                ]
            }}
        ]
    }}
    IMPORTANT: 'cost' must be an integer (USD) per group for that specific item.
    """

    messages = [
        SystemMessage(content="You are a JSON-only AI. Output valid JSON only."),
        HumanMessage(content=prompt)
    ]

    try:
        response = llm.invoke(messages)
        content = response.content.replace("```json", "").replace("```", "")
        return json.loads(content)
    except Exception as e:
        print("Error:", e)
        return {"error": "Agent failed"}

@app.post("/replace_activity")
async def replace_activity(req: ReplaceRequest):
    """
    Finds a replacement activity.
    """
    print(f"🔄 Swapping: {req.old_activity}")
    
    prompt = f"""
    User is in {req.destination}. They REJECTED: "{req.old_activity}".
    Suggest ONE alternative matching style: {req.experience}.
    
    Return strictly valid JSON:
    {{
        "time": "Keep original time",
        "activity": "New Activity Name", 
        "description": "Why this is better", 
        "cost": 30
    }}
    """
    
    messages = [SystemMessage(content="JSON only."), HumanMessage(content=prompt)]
    
    try:
        response = llm.invoke(messages)
        content = response.content.replace("```json", "").replace("```", "")
        return json.loads(content)
    except Exception as e:
        return {"error": "Failed to swap"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)