import os
from openai import OpenAI
from app.env import EmailEnv
from app.models import Action

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("API_BASE_URL")
)

env = EmailEnv()

# Step 1: Reset environment
obs = env.reset()
email_text = obs.email_text

print("Email:", email_text)

# Step 2: Try LLM call (safe fallback)
try:
    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[
            {
                "role": "user",
                "content": f"Classify this email as spam, normal, or urgent and suggest action (ignore, reply, escalate): {email_text}"
            }
        ]
    )

    reply = response.choices[0].message.content.lower()
    print("LLM Response:", reply)

except Exception as e:
    print("LLM failed, using fallback:", str(e))
    reply = "normal"

# Step 3: Convert response → action
if "urgent" in reply:
    action = Action(label="urgent", action="escalate")
elif "spam" in reply:
    action = Action(label="spam", action="ignore")
else:
    action = Action(label="normal", action="reply")

# Step 4: Step environment
_, reward, done, _ = env.step(action)

# Step 5: Print result
print("Chosen Action:", action)
print("Final Score:", reward.score)
print("Done:", done)