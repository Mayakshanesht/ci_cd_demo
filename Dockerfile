FROM python:3.9

WORKDIR /app

# Copy application files
COPY project.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 5002

CMD ["python3", "project.py"]
