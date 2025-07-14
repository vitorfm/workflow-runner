run-api:
	uvicorn app.main:app --reload

run-cli:
	python -m app.cli run test

test:
	PYTHONPATH=$(pwd) pytest

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt -r dev-requirements.txt