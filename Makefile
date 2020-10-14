PIPENV_CMD ?= pipenv run

all: init fmt sync test syntax tests

init:
	pip show -q pipenv || pip install --user pipenv
	pipenv lock --pre
	pipenv install
	pipenv install --dev
	${PIPENV_CMD} python setup.py --version

fmt:
	${PIPENV_CMD} black .

sync:
	${PIPENV_CMD} pipenv-setup sync
	${PIPENV_CMD} pipenv-setup sync --dev
	${PIPENV_CMD} python setup.py --version

docs:
	${PIPENV_CMD} sphinx-build -b html docs docs/_build/html

test:
	${PIPENV_CMD} coverage run -m unittest discover
	${PIPENV_CMD} coverage report -m

syntax:
	${PIPENV_CMD} flake8 wildq --count --exit-zero --statistics
	${PIPENV_CMD} bandit -r wildq

build:
	${PIPENV_CMD} python setup.py --version
	cat wildq/_wildq_version.py
	${PIPENV_CMD} python setup.py bdist_wheel

binary:
	${PIPENV_CMD} pyinstaller --clean --onefile --hidden-import=pkg_resources.py2_warn --name wildq wildq/__main__.py
	chmod +x dist/wildq
	cp dist/wildq dist/wq
	./tests/tests.sh

pypi:
	${PIPENV_CMD} python setup.py register -r pypi
	${PIPENV_CMD} python setup.py sdist upload -r pypi

clean:
	rm -rf dist build .eggs wildq.egg-info

.PHONY: all fmt init sync docs tests syntax build binary pypi clean
