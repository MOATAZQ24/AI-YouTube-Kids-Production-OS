FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p /app/state /app/outputs /app/knowledge /app/prompts /app/agents

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV APP_ENV=production

# Run the main orchestrator script
CMD ["python", "main.py"]
