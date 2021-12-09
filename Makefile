install:
	poetry install

gendiff:
	poetry run gendiff tests/file1.json tests/file2.json

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests

test:
	poetry run pytest

check: test lint

coverage:
	poetry run coverage xml
