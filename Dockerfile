# FROM python:3.9

# WORKDIR /app

# # Copy application files
# COPY project.py /app/
# COPY requirements.txt /app/

# # Install dependencies
# RUN pip install --no-cache-dir -r /app/requirements.txt

# EXPOSE 5002

# CMD ["python3", "project.py"]
FROM python:3.9

WORKDIR /app

# Download ImageNet class index file
RUN wget https://raw.githubusercontent.com/raghakot/keras-vis/master/resources/imagenet_class_index.json -O /app/imagenet_class_index.json

# Copy application files
COPY project.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 5002

CMD ["python3", "project.py"]