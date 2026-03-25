from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
import json, os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")
SETTINGS_FILE = os.path.join(os.path.dirname(__file__), "settings.json")

def read_data():
    if not os.path.exists(DATA_FILE):
        return {"goals": [], "lastApplied": None}
    with open(DATA_FILE) as f:
        return json.load(f)

def write_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def read_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {}
    with open(SETTINGS_FILE) as f:
        return json.load(f)

class Goal(BaseModel):
    id: int
    name: str
    current: float
    target: float
    monthly: float


class SavePayload(BaseModel):
    goals: list[Goal]
    lastApplied: Optional[str] = None


@app.get("/api/goals")
def get_goals():
    return read_data()


@app.put("/api/goals")
def save_goals(payload: SavePayload):
    write_data(payload.model_dump())
    return {"ok": True}

@app.get("/api/settings")
def get_settings():
    return read_settings()

# Serve the frontend from /frontend if it exists
frontend_dir = os.path.join(os.path.dirname(__file__), "..", "frontend")
if os.path.isdir(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="static")
