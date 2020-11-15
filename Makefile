install:
	poetry install

req:
	poetry export -f requirements.txt > requirements.txt

lint:
	poetry run flake8 http_file_repo

test:
	poetry run pytest --cov=http_file_repo --cov-report xml tests/

check: lint test

local:
	poetry run python http_file_repo/app.py

run:
	poetry run bash -c "gunicorn --bind 0.0.0.0:8001 http_file_repo.wsgi:app --daemon"

stop:
	./stop.sh