install:
	poetry install

gendiff1:
	poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

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
	poetry run coverage run -m pytest -v
	poetry run coverage xml

