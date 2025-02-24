FROM python:3.11-alpine
WORKDIR /app/backend
COPY . /app/backend
RUN apk add --no-cache gcc python3-dev musl-dev linux-headers
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
EXPOSE 5000
