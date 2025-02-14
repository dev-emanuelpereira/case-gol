FROM python:3.11-alpine
WORKDIR /case-gol
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
EXPOSE 5000
