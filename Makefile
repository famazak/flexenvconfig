.PHONY: test
test:
	poetry run pytest

.PHONY: install
install:
	poetry install --group dev
