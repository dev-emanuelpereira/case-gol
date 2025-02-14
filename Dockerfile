FROM python:3.14.0a5-alpine3.20
WORKDIR /case-gol
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
EXPOSE 5000
