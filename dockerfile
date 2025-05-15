FROM python:3.13.2-slim

# Install dependencies for adding the Microsoft repository
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends apt-transport-https ca-certificates curl gnupg lsb-release && \
    curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | tee /etc/apt/trusted.gpg.d/microsoft.asc.gpg > /dev/null && \
    AZ_REPO=$(lsb_release -cs) && \
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | tee /etc/apt/sources.list.d/azure-cli.list && \
    apt-get update -y && \
    apt-get install -y azure-cli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy your project files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Set the command to run your Python app
CMD ["python3", "app.py"]
