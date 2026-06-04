FROM python:3.13.11-alpine
WORKDIR /temperature-converter-cli
COPY main.py .
ENTRYPOINT ["python", "main.py"]
