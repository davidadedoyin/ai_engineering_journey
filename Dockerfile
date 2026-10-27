
FROM python:3.12-slim

# Prevent Python from creating unnecessary cache files.
ENV PYTHONDONTWRITEBYTECODE=1

# Make Python logs appear immediately in Docker.
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container.
WORKDIR /app

# Copy the dependency list into the container.
COPY requirements.txt .

# Install the Python packages our application needs.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container.
COPY . .

# Document the port used by the application.
EXPOSE 10000

# Start the FastAPI application.
CMD ["sh", "-c", "uvicorn projects.month7_llm_assistant.app:app --host 0.0.0.0 --port ${PORT:-8000}"]
