PIPENV_CMD ?= pipenv run

PYTHON_WILDQ_VERSION := $(shell sed -n -e 's/^version = "\(.*\)\.\(.*\)\.\(.*\)"/\1.\2.\3/p' wildq/_wildq_version.py)

all: init fmt sync test syntax tests

init:
	pip show -q pipenv || pip install pipenv
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

docs: sync
	${PIPENV_CMD} sphinx-build -b html docs docs/_build/html

test: sync
	${PIPENV_CMD} coverage run -m unittest discover
	${PIPENV_CMD} coverage report -m

syntax: sync
	${PIPENV_CMD} flake8 wildq --count --exit-zero --statistics
	${PIPENV_CMD} bandit -r wildq

build: sync
	${PIPENV_CMD} python setup.py --version
	cat wildq/_wildq_version.py
	${PIPENV_CMD} python setup.py bdist_wheel
	mkdir -p artifacts/archives
	mkdir -p artifacts/binaries
	mkdir -p artifacts/brew
	mkdir -p artifacts/deb
	mkdir -p artifacts/rpm

binary: build
	${PIPENV_CMD} pyinstaller --distpath artifacts/binaries --clean --onefile --name wildq wildq/__main__.py
	chmod +x artifacts/binaries/wildq
	cp artifacts/binaries/wildq artifacts/binaries/wq
	cp README.md LICENSE artifacts/binaries
	./tests/tests.sh

archive-linux: binary
	tar cfz artifacts/archives/wildq-$(PYTHON_WILDQ_VERSION)-linux-x86_64.tar.gz -C artifacts/binaries wq wildq README.md LICENSE
	sha256sum artifacts/archives/wildq-$(PYTHON_WILDQ_VERSION)-linux-x86_64.tar.gz

archive-macos: binary
	tar cfz artifacts/archives/wildq-$(PYTHON_WILDQ_VERSION)-darwin-x86_64.tar.gz -C artifacts/binaries wq wildq README.md LICENSE
	sha256sum artifacts/archives/wildq-$(PYTHON_WILDQ_VERSION)-darwin-x86_64.tar.gz

package-rpm: archive-linux
	mkdir -p artifacts/rpm/usr/bin/
	cp artifacts/binaries/wildq artifacts/rpm/usr/bin/wildq
	cp artifacts/binaries/wildq artifacts/rpm/usr/bin/wq
	cd artifacts/rpm/; fpm \
		--input-type dir \
		--output-type rpm \
		--version $(PYTHON_WILDQ_VERSION) \
		--iteration 1 \
		--prefix / \
		--name wildq \
		--rpm-user root \
		--rpm-attr "755,root,root:/usr/bin/wildq" \
		--rpm-attr "755,root,root:/usr/bin/wq" \
		.

package-deb: archive-linux
	mkdir -p artifacts/deb/usr/bin/
	cp artifacts/binaries/wildq artifacts/deb/usr/bin/wildq
	cp artifacts/binaries/wildq artifacts/deb/usr/bin/wq
	cd artifacts/deb/; fpm \
		--input-type dir \
		--output-type deb \
		--version $(PYTHON_WILDQ_VERSION) \
		--iteration 1 \
		--prefix / \
		--name wildq \
		--deb-user root \
		.

package-brew: archive-macos
	echo "FIXME: auto update my homebrew-tap repo"

pypi:
	${PIPENV_CMD} python setup.py register -r pypi
	${PIPENV_CMD} python setup.py sdist upload -r pypi

clean:
	git clean -fdx

.PHONY: all fmt init sync docs tests syntax build binary pypi clean
