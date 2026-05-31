# Sentiment Analysis API

A simple sentiment analysis API built with Flask and scikit-learn.

## Project Structure
- `app/`: Core logic for model loading and predictions.
- `model/`: Directory containing the trained model file.
- `server.py`: Flask server implementation.
- `train.py`: Script to train the model.
- `requirements.txt`: Project dependencies.

## Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Training the Model
If you need to retrain the model:
```bash
python train.py
```

### Running the API

#### Local Development
```bash
python server.py
```
The server will run on `http://localhost:5001`.

#### Production (Gunicorn)
```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 server:app
```

#### Using Docker
```bash
docker build -t sentiment-api .
docker run -p 5000:5000 sentiment-api
```

## API Endpoints

### Health Check
- **Endpoint:** `GET /health`
- **Response:** `{"status": "ok"}`

### Predict Sentiment
- **Endpoint:** `POST /predict`
- **Request Body:**
  ```json
  {
    "text": "I love this product!"
  }
  ```
- **Response:**
  ```json
  {
    "text": "I love this product!",
    "sentiment": "positive",
    "confidence": 0.98
  }
  ```
