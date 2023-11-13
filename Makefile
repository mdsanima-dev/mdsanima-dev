# Copyright (c) 2023 MDSANIMA

# This is Makefile helper for test, build, install, and more.


.PHONY: test build

all: test build

test:
	python -m pytest

build:
	python -m build

sphinx:
	sphinx-build -M dirhtml docs build

clean:
	rm -rf build/dirhtml build/doctrees
	mkdir build/dirhtml build/doctrees

install:
	pip install .

wheel:
	pip wheel --wheel-dir dist --no-deps .
