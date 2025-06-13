# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the dependencies file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code
COPY . .

# Gunicorn will bind to the port provided by the $PORT environment variable
# This is automatically supplied by Cloud Run.
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "main:app"]
