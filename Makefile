dev:
	python3 src/app.py

build:
	poetry install && export FLASK_APP=src/app.py

test_unit:
	poetry run pytest ./tests/unit

test_integration:
	poetry run pytest ./tests/integration

test:
	poetry run pytest ./tests

lint:
	poetry run pylint ./src

format:
	poetry run black ./src && poetry run isort ./src
