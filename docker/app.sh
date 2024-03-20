#!/bin/bash

sleep 3

# alembic revision --autogenerate -m 'MIGRATE'

alembic upgrade head

uvicorn src.main:app --host 0.0.0.0 --port 8000