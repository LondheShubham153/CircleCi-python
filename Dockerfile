FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
EXPOSE 80
ENTRYPOINT ["python3", "main.py"]
