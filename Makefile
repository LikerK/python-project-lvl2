gendiff:
	poetry run gendiff tests/file1.json tests/file2.json

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff