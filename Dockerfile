FROM python:3.9

WORKDIR /app

COPY project.py .
COPY requirements.txt .  # Ensure the requirements.txt file is available

# Install dependencies
RUN pip install -r requirements.txt
EXPOSE 80

CMD ["python3", "project.py"]