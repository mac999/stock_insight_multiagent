# Insight Agent Lite

A lightweight multi-role AI assistant for overseas stock research. Designed for local PCs with 8GB VRAM running a quantized Llama 3 8B model via [Ollama](https://github.com/ollama/ollama).

This repository provides a minimal skeleton implementation, featuring a Gradio-based chat UI and a placeholder agent using LangChain-compatible patterns.

## Requirements
- Python 3.10+
- The `ollama` runtime with `llama3:8b` model installed

Install dependencies:
```bash
pip install -r requirements.txt
```

## Running
```bash
python app.py
```

This launches a local Gradio interface where you can chat with the agent, upload PDF files, and configure API keys.
