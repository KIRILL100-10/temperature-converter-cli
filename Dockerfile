FROM python:3.13.11-alpine
WORKDIR /temperature-converter-cli
COPY . .
CMD ["python", "main.py"]
