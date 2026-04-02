import gradio as gr
import requests

BASE_URL = "https://sparkgen0markvi-meta-pytorch-hackathon.hf.space"


# ---------- API FUNCTIONS ----------

def reset_env():
    res = requests.post(f"{BASE_URL}/reset")
    return res.json()


def get_state():
    res = requests.get(f"{BASE_URL}/state")
    return res.json()


def take_action(label, action):
    payload = {"label": label, "action": action}
    res = requests.post(f"{BASE_URL}/step", json=payload)
    return res.json()


def grade_action(label, action):
    payload = {"label": label, "action": action}
    res = requests.post(f"{BASE_URL}/grader", json=payload)
    return res.json()


def get_baseline():
    res = requests.get(f"{BASE_URL}/baseline")
    return res.json()


# ---------- UI ----------

with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue")) as demo:

    gr.Markdown("# 🚀 OpenEnv Dashboard (Dark Mode)")

    # Guide Section
    gr.Markdown("""
    ## 📘 How to Use

    🔄 **Step 1: Reset Environment**  
    Start fresh by clicking **Reset**

    📊 **Step 2: Check State**  
    View current situation of environment

    ⚡ **Step 3: Take Action**
    - Choose **Label** → spam / normal / urgent  
    - Choose **Action** → ignore / process  
    - Click **Execute**

    📈 **Step 4: Evaluate**
    - Use **Grade** to check correctness
    - Compare with **Baseline**

    🎯 **Goal:**  
    Take correct actions → maximize score → beat baseline
    """)

    gr.Markdown("---")

    # Top Buttons
    with gr.Row():
        reset_btn = gr.Button("🔄 Reset Environment")
        state_btn = gr.Button("📊 Get State")
        baseline_btn = gr.Button("📈 Baseline")

    output = gr.JSON(label="Output")

    reset_btn.click(reset_env, outputs=output)
    state_btn.click(get_state, outputs=output)
    baseline_btn.click(get_baseline, outputs=output)

    gr.Markdown("## ⚡ Take Action")

    with gr.Row():
        label = gr.Dropdown(
            ["spam", "normal", "urgent"],
            label="Label",
            value="normal"
        )

        action = gr.Dropdown(
            ["ignore", "process"],
            label="Action",
            value="ignore"
        )

    with gr.Row():
        action_btn = gr.Button("🚀 Execute Action")
        grade_btn = gr.Button("🧠 Grade Action")

    action_btn.click(take_action, inputs=[label, action], outputs=output)
    grade_btn.click(grade_action, inputs=[label, action], outputs=output)


# Run app
demo.launch()
