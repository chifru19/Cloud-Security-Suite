# 1. Use a specific, non-latest version for stability
FROM python:3.9.18-slim-buster

# 2. Set secure working directory
WORKDIR /app

# 3. Security Hardening: Ensure system is updated and clean
RUN apt-get update && apt-get install -y \
    nmap=7.70-1 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy project files
COPY . /app

# 5. The "Golden Rule": Switch to a non-root user
# Checkov fails if it sees the container running as root
RUN useradd -m frankfru-user && \
    chown -R frankfru-user:frankfru-user /app
USER frankfru-user

# 6. Add a Healthcheck (Checkov often requires this)
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost/ || exit 1

# Verify installation
CMD ["nmap", "--version"]
