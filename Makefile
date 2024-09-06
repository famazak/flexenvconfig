.PHONY: test
test:
	poetry run pytest

.PHONY: install
install:
	poetry install --group dev

.PHONY: build
build:
	poetry build

.PHONY: publish
publish:
	poetry publish --build

.PHONY: lint
lint:
	poetry run mypy flexenvconfig;  poetry run ruff check flexenvconfig
