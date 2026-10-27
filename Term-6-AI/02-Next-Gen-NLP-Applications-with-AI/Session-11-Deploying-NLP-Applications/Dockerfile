# Session 11 - Example 6: package the API in a Docker container
# Build: docker build -t sentiment-api .
# Run:   docker run -p 8000:8000 sentiment-api

# Step 1: start from a small official Python image
FROM python:3.12-slim

# Step 2: work inside /app
WORKDIR /app

# Step 3: install dependencies first (Docker caches this layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: copy the code and train the model inside the image
COPY train_and_save_model.py predict.py app_fastapi.py ./
RUN python train_and_save_model.py

# Step 5: start the web server on port 8000
EXPOSE 8000
CMD ["uvicorn", "app_fastapi:app", "--host", "0.0.0.0", "--port", "8000"]
