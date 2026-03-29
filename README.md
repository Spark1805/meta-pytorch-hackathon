# 🚀 Meta PyTorch Hackathon – OpenEnv Project

A modular AI environment + inference system built using **PyTorch** and aligned with **Meta’s OpenEnv framework**.

---

## 🧠 What This Project Does

This project provides:

* AI agent experimentation environment
* Modular ML pipeline design
* API-based model inference
* Containerized deployment setup

Designed for rapid prototyping and hackathon workflows.

---

## ⚡ Key Features

* 🧩 Modular architecture
* ⚡ FastAPI-based inference
* 🧠 PyTorch integration
* 🐳 Docker-ready
* 🔁 Reproducible environments

---

## 🏗️ Project Structure

```id="tree2"
.
├── api/
│   └── main.py
│
├── app/
│   ├── data.py
│   ├── models.py
│   ├── tasks.py
│   ├── utils.py
│   └── env.py
│
├── inference.py
├── requirements.txt
├── openenv.yaml
├── Dockerfile
└── README.md
```

---

## ⚙️ Setup

```bash id="clone2"
git clone https://github.com/Spark1805/meta-pytorch-hackathon.git
cd meta-pytorch-hackathon
```

### Install dependencies

**Conda:**

```bash id="conda2"
conda env create -f openenv.yaml
conda activate openenv
```

**Pip:**

```bash id="pip2"
pip install -r requirements.txt
```

---

## ▶️ Run

### API

```bash id="run2"
uvicorn api.main:app --reload
```

### Inference

```bash id="infer2"
python inference.py
```

---

## 🐳 Docker

```bash id="docker2"
docker build -t openenv-app .
docker run -p 8000:8000 openenv-app
```

---

## 📡 API Endpoints

| Endpoint   | Method | Description     |
| ---------- | ------ | --------------- |
| `/`        | GET    | Health check    |
| `/predict` | POST   | Model inference |

---

## 🧠 Tech Stack

* PyTorch
* FastAPI
* Docker
* Python

---

## 🎯 Hackathon Context

Built for the **Meta x PyTorch OpenEnv Hackathon**, focusing on:

* AI environments
* Agent workflows
* Scalable ML systems

---

## ⚠️ Usage

This repository is shared for **viewing and reference purposes only**.
Reuse, modification, or distribution is not permitted without explicit permission.

---
