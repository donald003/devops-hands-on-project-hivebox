FROM python:3.11-alpine
WORKDIR /app
COPY hivebox_app.py .
CMD ["python", "hivebox_app.py"]