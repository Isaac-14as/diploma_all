#!/bin/bash

alembic upgrade head


gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

# gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000git  --certfile=cert.pem --keyfile=key.pem --forwarded-allow-ips="*"