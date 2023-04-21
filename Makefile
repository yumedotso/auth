dev:
	poetry run python3 src/app.py

build:
	poetry install && export FLASK_APP=src/app.py

test_unit:
	poetry run  pytest ./tests/services

test_int:
	poetry run python3 -m unittest discover -s ./tests/routes -v

test:
	poetry run python3 -m unittest discover -s ./tests

lint:
	poetry run pylint ./src

format:
	poetry run black ./src && poetry run isort ./src
