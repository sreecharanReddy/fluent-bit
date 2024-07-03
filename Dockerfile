FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script
COPY app.py .

# Install dependencies (if any)
# RUN pip install ...

# Create a directory for logs
RUN mkdir -p /logs

# Run the Python application
CMD ["python", "app.py"]
