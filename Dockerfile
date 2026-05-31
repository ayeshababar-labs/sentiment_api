# Use a slim Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy and install dependencies first (layer caching optimization)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Run with gunicorn (4 worker processes)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "server:app"]