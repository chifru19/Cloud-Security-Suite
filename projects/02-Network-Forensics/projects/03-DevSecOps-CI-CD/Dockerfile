# Use a secure, minimal base image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Install security tools & clean up to reduce image size
RUN apt-get update && apt-get install -y \
    nmap \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy local files into the container
COPY . /app

# Create a non-root user for security (Least Privilege Principle)
RUN useradd -m frankfru-sec
USER frankfru-sec

# Verify the installation on startup
CMD ["nmap", "--version"]
