# 🩺 Local AI Health & Diagnostic Chatbot

An interactive health advisory chat application built using **Streamlit** and running private, local LLMs via **Ollama**.

## 📌 Features
- **Strict Guardrails**: Includes a system prompt forcing AI disclaimers and emergency advice safety rules.
- **Stateful Memory**: Maintains chat context across multiple user inputs.
- **Real-time Streaming**: Renders responses token-by-token directly from local Ollama models.
- **Privacy First**: All queries run locally on your hardware without sending data to third-party API providers.

---

## 🛠️ Requirements
- Python 3.9+
- [Ollama App](https://ollama.com/) installed and running locally
- Python libraries specified in `Requirements.txt`:
  - `streamlit==1.58.0`
  - `ollama` Python client library

---

## 🚀 Setup & Installation

### 1. Prepare Local AI Model
Ensure Ollama is running, then pull your preferred model via terminal:
```bash
ollama pull llama3