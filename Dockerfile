FROM python:3.9

WORKDIR /app

COPY project.py /app/
COPY requirements.txt /app/  # Ensure the requirements.txt file is available

# Install dependencies
RUN pip install  --no-cache-dir -r /app/requirements.txt
EXPOSE 80

CMD ["python3", "project.py"]