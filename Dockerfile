# Base image with Python 3.9 slim version
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Install essential system dependencies
RUN apt-get update && apt-get install -y \
    git \
    wget \
    ffmpeg \
    build-essential \
    libsm6 \
    libxext6 \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Download the pre-trained U-2-Net model from Google Drive
RUN mkdir -p saved_models/u2net && \
    wget --no-check-certificate "https://drive.google.com/uc?id=1rbSTGKAE-MTxBYHd-51l2hMOQPT_7EPy" -O saved_models/u2net/u2net.pth

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
    numpy \
    scikit-image \
    torch torchvision \
    pillow \
    opencv-python-headless \
    gradio

# Expose the default Gradio port
EXPOSE 7860

# Set the default command to run the application
CMD [ "python", "app.py" ]
