FROM python:3.11-slim

# Install system libraries for Chromium and Playwright
RUN apt-get update && apt-get install -y \
    libnss3 libatk-bridge2.0-0 libxss1 libasound2 libx11-xcb1 libgtk-3-0 \
    libdrm2 libxdamage1 libxcomposite1 libgbm1 libxrandr2 libu2f-udev \
    libxshmfence1 libxext6 libxi6 libxtst6 fonts-liberation \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install the requirements package and copy application
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
RUN playwright install --with-deps chromium
COPY src/ .
CMD ["python", "-m", "main"]
