from fastapi import FastAPI
from app.env import EmailEnv
from app.models import Action

app = FastAPI()
env = EmailEnv()

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: Action):
    return env.step(action)

@app.get("/state")
def state():
    return env.state()

@app.get("/tasks")
def tasks():
    return {
        "tasks": ["easy", "medium", "hard"],
        "actions": ["spam", "normal", "urgent"]
    }

@app.post("/grader")
def grader(action: Action):
    current = env.state()

    if current is None:
        return {"error": "Call /reset first"}

    actual = current["label"]

    if action.label == actual:
        score = 1.0
    else:
        score = 0.0

    return {"score": score}

@app.get("/baseline")
def baseline():
    obs = env.reset()
    action = {"label": "normal", "action": "ignore"}
    _, reward, _, _ = env.step(Action(**action))
    return {"baseline_score": reward.score}
