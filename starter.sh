#!/bin/bash

while [ $# -gt 0 ] ; do
  case $1 in
    -t | --target) W="$2" ;;
  esac
  shift
done

case $W in
    worker) poetry run celery -A src.api.main.celery worker --loglevel=info;;
    flower) poetry run celery -A src.api.main.celery flower --port=5555;;
    fastapi) poetry run python src/api/main.py;;
esac
