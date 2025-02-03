FROM python:3.9

WORKDIR /app

COPY project.py .

CMD ["python3", "project.py"]