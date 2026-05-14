# 1. Use a specific version to avoid 'latest' tag vulnerabilities
FROM python:3.9.18-slim-buster

# 2. Set working directory
WORKDIR /app

# 3. Install tools with version pinning
RUN apt-get update && apt-get install -y --no-install-recommends \
    nmap=7.70-1 \
    curl=7.64.0-4+deb10u9 \
    && rm -rf /var/lib/apt/lists/*

# 4. Create a specific System User with a defined UID (Checkov requirement)
RUN groupadd -g 10001 frankgroup && \
    useradd -u 10001 -g frankgroup -m frankuser

# 5. Copy files and set ownership
COPY --chown=frankuser:frankgroup . /app

# 6. Add a Healthcheck (This is usually why the scan fails)
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1

# 7. Switch to the non-privileged user
USER 10001

# Default command
CMD ["nmap", "--version"]
