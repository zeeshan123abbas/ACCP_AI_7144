# Small, reproducible image for the grade service
FROM python:3.12-slim
WORKDIR /app
COPY server.py app.py ./
EXPOSE 8000
CMD ["python", "server.py"]
