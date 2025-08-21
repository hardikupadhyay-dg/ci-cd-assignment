FROM python:3.12-slim
WORKDIR /app
# Only copy package code (not tests)
COPY calcapp/ ./calcapp/
COPY pyproject.toml requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir .
# Example default command (no server, just a placeholder)
CMD ["python", "-c", "import calcapp; print('calcapp ready')"]
