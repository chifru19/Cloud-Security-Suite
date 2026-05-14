# Step 1: Use a minimal, secure base image
FROM python:3.9-slim-buster

# Step 2: Set a secure working directory
WORKDIR /app

# Step 3: Install only essential security tools
# We combine commands and clean the cache to keep the image small
RUN apt-get update && apt-get install -y \
    nmap \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Copy project files (even if empty, this establishes the structure)
COPY . /app

# Step 5: Security Hardening - Create and switch to a non-root user
# This prevents attackers from gaining full control of the host if the app is breached
RUN useradd -m frankfru-sec
USER frankfru-sec

# Step 6: Default command to verify the tool is working
CMD ["nmap", "--version"]
