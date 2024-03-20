FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

COPY . .

RUN chmod a+x *.sh

# ENTRYPOINT [ "sh", "app.sh" ]
CMD uvicorn src.main:app --host 0.0.0.0 --port 8000