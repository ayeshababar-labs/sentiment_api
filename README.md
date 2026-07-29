# Agentic Sentiment Analysis System

An integrated system comprising a specialized sentiment analysis API and an agentic layer that utilizes this API as a tool for autonomous reasoning and text analysis.

## System Architecture

### 1. Sentiment Analysis API
A production-ready microservice that provides sentiment classification.
- **Core:** Built with Flask and HuggingFace Transformers.
- **Model:** DistilBERT fine-tuned on SST-2 (`distilbert-base-uncased-finetuned-sst-2-english`).
- **Deployment:** Containerized via Docker and scalable using Gunicorn.

### 2. Agentic Layer
An implementation of AI agents that treat the Sentiment API as an external tool.
- **Orchestration:** Agents use LLMs to determine when to invoke the `/predict` endpoint to analyze text.
- **Providers:** Experimental implementations using Groq (cloud-based) and Ollama (local).
- **Workflows:** Autonomous decision-making loops where the agent fetches sentiment data before generating a final synthesis or response.

## Project Structure
- `app/`: Model loading and prediction logic.
- `model/`: Trained model artifacts.
- `server.py`: Flask API implementation.
- `experiments/`: Agentic implementations:
    - `01_groq_hello.py` & `02_groq_tool.py`: Groq-based agent tool integration.
    - `03_ollama_tool.py` & `05_ollama_real_tool.py`: Local agent integration via Ollama.
    - `04_real_tool.py`: Integration of the live API as a functional tool.
- `Dockerfile`: API container configuration.
- `requirements.txt`: System dependencies.

## Setup and Execution

### Installation
```bash
pip install -r requirements.txt
```

### Running the API
**Local:**
```bash
python server.py
```
**Production:**
```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 server:app
```
**Docker:**
```bash
docker build -t sentiment-api .
docker run -p 5000:5000 sentiment-api
```

### Agent Execution Setup

**1. Groq Setup:**
- Obtain a Groq API key from [Groq Console](https://console.groq.com/).
- Set it as an environment variable:
  ```bash
  export GROQ_API_KEY='your_api_key_here'

**2. Ollama Setup (for local agents):**
- Install Ollama from [ollama.com](https://ollama.com)
- Start the Ollama server:
  ```bash
  ollama serve
  ```
- Pull the required model (in a separate terminal):
  ```bash
  ollama pull llama3.1
  ```


### Agent Execution
To run the agentic experiments, ensure the API is running first.

**Groq-based Agents:**
```bash
python experiments/02_groq_tool.py
python experiments/04_real_tool.py
```

**Ollama-based Agents (Local):**
```bash
python experiments/03_ollama_tool.py
python experiments/05_ollama_real_tool.py
```


## API Reference

### Predict Sentiment
- **Endpoint:** `POST /predict`
- **Request:** `{"text": "string"}`
- **Response:** `{"text": "string", "sentiment": "positive/negative", "confidence": float}`

### Health Check
- **Endpoint:** `GET /health`
- **Response:** `{"status": "ok"}`
