# Base image with Python 3.7
FROM python:3.7-slim

# Disable interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install basic development tools
RUN apt-get update && apt-get install -y \
  git \
  curl \
  build-essential \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

# Create the "vscode" user required for Dev Containers
RUN useradd -m vscode

# Switch to non-root user
USER vscode

# Default working directory inside the container
WORKDIR /workspace

# Upgrade pip to a version compatible with Python 3.7
RUN pip install --upgrade "pip<22" setuptools wheel
