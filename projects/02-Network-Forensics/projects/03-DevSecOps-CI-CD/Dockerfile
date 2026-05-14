# Use a lightweight Python base image
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Install basic security tools and dependencies
RUN apt-get update && apt-get install -y \
    nmap \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy your local scripts into the container
# (Even if the folder is empty now, this sets up the structure)
COPY . /app

# Create a non-privileged user for security best practices
RUN useradd -m security-user
USER security-user

# The command to run when the container starts
CMD ["nmap", "-V"]
