# Base image with CUDA support
FROM pytorch/pytorch:2.2.0-cuda12.1-cudnn8-runtime

# Avoid interactive installs
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /workspace

# Install system packages
RUN apt-get update && apt-get install -y \
    git \
    wget \
    curl \
    vim \
    python3-pip \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install paddlepaddle-gpu from official CUDA 12.1 wheel
# (PyPI only carries CPU/generic builds; CUDA builds are on paddle's own index)
RUN pip install paddlepaddle-gpu==2.6.1 \
    -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html \
    --no-cache-dir

# Copy and install remaining requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Default command
CMD ["bash"]
