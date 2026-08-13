FROM python:3.11-alpine
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY hivebox_app.py .
EXPOSE 5000

USER 65534

CMD ["python", "hivebox_app.py"]
