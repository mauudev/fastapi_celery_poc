shell:
	poetry shell

install:
	poetry install

run:
	poetry run python src/api/main.py

ipython:
	poetry run ipython

clean-pyc:
	find . -type d -name '__pycache__' -exec rm -rf {} \; || exit 0
	find . -type f -iname '*.pyc' -delete || exit 0

build:
	poetry build

test:
	poetry run pytest tests

test_debug:
	poetry run pytest -vvs tests

test_one:
	poetry run pytest ${t} -vvs

test_coverage:
	poetry run pytest --cov=src tests/

docker-run:
	docker-compose -f ${PWD}/docker-compose.yml up -d

docker-run-build:
	docker-compose -f ${PWD}/docker-compose.yml up -d --build

docker-stop:
	docker-compose -f ${PWD}/docker-compose.yml down

format:
	poetry run black src tests


.PHONY: install start clean test build
