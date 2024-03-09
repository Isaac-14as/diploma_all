FROM python:3.11.8

RUN mkdir /diploma

WORKDIR /diploma

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /diploma/docker/*.sh

# CMD ["sh /diploma/docker/app.sh"]

# CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]