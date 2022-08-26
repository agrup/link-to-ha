FROM python:3.4

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONPYCACHEPREFIX=/tmp


COPY requirements.txt .

RUN pip install -r requirements.txt


ENV PYTHONUNBUFFERED=1
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
