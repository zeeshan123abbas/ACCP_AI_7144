# Campus Help Desk Assistant - container image
# Build: docker build -t helpdesk-bot .
# Run:   docker run -p 8000:8000 -e OPENAI_API_KEY=your-key-here helpdesk-bot
#        (leave out -e OPENAI_API_KEY to run in offline mock mode)
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY *.py ./
RUN python test_assistant.py
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
