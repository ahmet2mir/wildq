PYTHON_CMD ?= python
PIP_CMD ?= pip

all: init_pipx test build binary-linux binary-tests archive-linux package-rpm package-deb

# lists all available targets
list:
	@sh -c "$(MAKE) -p no_targets__ | \
		awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {\
			split(\$$1,A,/ /);for(i in A)print A[i]\
		}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"

# required for list
no_targets__:

init_pip:
	@echo "Target init_pip"
	$(PIP_CMD) show -q poetry || $(PIP_CMD) install poetry
	$(PIP_CMD) show -q poetry-dynamic-versioning || $(PIP_CMD) install poetry-dynamic-versioning
	poetry install
	poetry version --no-ansi
	poetry update --dry-run
	touch init_pip

init_pipx:
	@echo "Target init_pipx"
	$(PIP_CMD) show -q pipx || $(PIP_CMD) install pipx
	$(PYTHON_CMD) -m pipx ensurepath
	pipx runpip poetry show -q poetry || pipx install poetry
	pipx runpip poetry show -q  poetry-dynamic-versioning || pipx inject poetry poetry-dynamic-versioning
	poetry install
	poetry version --no-ansi
	poetry update --dry-run
	touch init_pipx

fmt:
	@echo "Target fmt"
	poetry run black wildq tests

poetry.lock:
	@echo "Target poetry.lock"
	poetry lock
	poetry version --no-ansi

docs: poetry.lock
	@echo "Target docs"
	poetry run sphinx-build -b html docs docs/_build/html

test: poetry.lock
	@echo "Target test"
	poetry run coverage run -m unittest discover
	poetry run coverage report -m

syntax: poetry.lock
	@echo "Target syntax"
	poetry run flake8 wildq --count --exit-zero --statistics
	poetry run bandit -r wildq

upx:
	@echo "Target upx"
	curl -sL https://github.com/upx/upx/releases/download/v3.96/upx-3.96-amd64_linux.tar.xz | tar -xJ -C .
	mv ./upx-3.96-amd64_linux upx

build: poetry.lock
	@echo "Target build"
	poetry version --no-ansi
	cat wildq/_wildq_version.py
	mkdir -p artifacts/archives
	mkdir -p artifacts/binaries
	mkdir -p artifacts/brew
	mkdir -p artifacts/deb
	mkdir -p artifacts/rpm
	poetry build

binary-linux: upx build
	@echo "Target binary"
	poetry run pyinstaller --upx-dir=upx --distpath artifacts/binaries --clean --onefile --name wildq wildq/__main__.py
	chmod +x artifacts/binaries/wildq
	cp artifacts/binaries/wildq artifacts/binaries/wq
	cp README.md LICENSE artifacts/binaries
	du -hs ./artifacts/binaries/pipeline

binary-macos: build
	@echo "Target binary"
	brew install upx
	ls /usr/local/Cellar/upx/3.96/bin
	poetry run pyinstaller --upx-dir=/usr/local/Cellar/upx/3.96/bin   --distpath artifacts/binaries --clean --onefile --name wildq wildq/__main__.py
	chmod +x artifacts/binaries/wildq
	cp artifacts/binaries/wildq artifacts/binaries/wq
	cp README.md LICENSE artifacts/binaries
	du -hs ./artifacts/binaries/pipeline

binary-tests: binary
	@echo "Target binary-tests"
	sh -e ./tests/tests.sh

archive-linux: binary
	@echo "Target archive-linux"
	tar cfz artifacts/archives/wildq-$(shell poetry version --no-ansi --short)-linux-x86_64.tar.gz -C artifacts/binaries wq wildq README.md LICENSE
	sha256sum artifacts/archives/wildq-$(shell poetry version --no-ansi --short)-linux-x86_64.tar.gz

archive-macos: binary
	@echo "Target archive-macos"
	tar cfz artifacts/archives/wildq-$(shell poetry version --no-ansi --short)-darwin-x86_64.tar.gz -C artifacts/binaries wq wildq README.md LICENSE
	sha256sum artifacts/archives/wildq-$(shell poetry version --no-ansi --short)-darwin-x86_64.tar.gz

package-rpm: archive-linux
	@echo "Target package-rpm"
	mkdir -p artifacts/rpm/usr/bin/
	cp artifacts/binaries/wildq artifacts/rpm/usr/bin/wildq
	cp artifacts/binaries/wildq artifacts/rpm/usr/bin/wq
	cd artifacts/rpm/; fpm \
		--input-type dir \
		--output-type rpm \
		--version $(shell poetry version --no-ansi --short) \
		--iteration 1 \
		--prefix / \
		--name wildq \
		--rpm-user root \
		--rpm-attr "755,root,root:/usr/bin/wildq" \
		--rpm-attr "755,root,root:/usr/bin/wq" \
		.

package-deb: archive-linux
	@echo "Target archive-linux"
	mkdir -p artifacts/deb/usr/bin/
	cp artifacts/binaries/wildq artifacts/deb/usr/bin/wildq
	cp artifacts/binaries/wildq artifacts/deb/usr/bin/wq
	cd artifacts/deb/; fpm \
		--input-type dir \
		--output-type deb \
		--version $(shell poetry version --no-ansi --short) \
		--iteration 1 \
		--prefix / \
		--name wildq \
		--deb-user root \
		.

package-brew: archive-macos
	@echo "Target package-brew"
	echo "FIXME: auto update my homebrew-tap repo"

pypi:
	@echo "Target pypi"
	poetry publish

clean:
	@echo "Target clean"
	git clean -fdx

clean-venv:
	@echo "Target clean-venv"
	@poetry env remove $$(poetry env list --no-ansi | tail -n 1 | cut -d' ' -f1)

.PHONY: all archive-linux archive-macos binary binary-linux binary-macos binary-tests build clean clean-venv docs fmt list package-brew package-deb package-rpm pypi syntax test 
