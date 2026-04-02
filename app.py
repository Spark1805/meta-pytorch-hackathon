import gradio as gr
from app.env import EmailEnv
from app.models import Action

env = EmailEnv()

def reset_env():
    return env.reset()


def get_state():
    return env.state()


def take_action(label, action):
    result = env.step(Action(label=label, action=action))
    return result


def grade_action(label, action):
    current = env.state()

    if current is None:
        return {"error": "Call reset first"}

    actual = current["label"]
    score = 1.0 if label == actual else 0.0

    return {"score": score}


def get_baseline():
    env.reset()
    action = Action(label="normal", action="ignore")
    _, reward, _, _ = env.step(action)
    return {"baseline_score": reward.score}


with gr.Blocks() as demo:

    gr.Markdown("# 🚀 OpenEnv Dashboard")

    gr.Markdown("""
    ## 📘 How to Use

    🔄 Reset → Initialize environment  
    📊 State → View current state  
    ⚡ Execute → Take action  
    🧠 Grade → Evaluate correctness  
    📈 Baseline → Compare performance  

    🎯 Goal: Maximize score by correct actions
    """)

    gr.Markdown("---")

    # Controls
    with gr.Row():
        reset_btn = gr.Button("🔄 Reset")
        state_btn = gr.Button("📊 State")
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
        exec_btn = gr.Button("🚀 Execute")
        grade_btn = gr.Button("🧠 Grade")

    exec_btn.click(take_action, inputs=[label, action], outputs=output)
    grade_btn.click(grade_action, inputs=[label, action], outputs=output)


demo.launch(server_name="0.0.0.0", server_port=7860)
