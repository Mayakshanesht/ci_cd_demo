FROM python:3.9

WORKDIR /app

COPY project.py .

EXPOSE 80

CMD ["python3", "project.py"]