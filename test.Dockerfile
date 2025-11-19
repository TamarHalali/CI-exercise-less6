FROM python:3.8-slim

RUN python -m pip install --upgrade pip
WORKDIR /app

COPY testserver.py .

RUN pip install requests
COPY requirements.txt .
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

CMD ["python", "testserver.py"]

