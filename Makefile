.PHONY: refresh build install build_dist json release lint test 

refresh: clean build install lint

build:
	python setup.py build

install:
	python setup.py install

lint:
	flake8 src/ tests/ --exclude 'src/zones.*' --count --ignore=W503 --max-line-length=127 --statistics
	mypy src/ --exclude 'src/zones.*'

test:
	python -m unittest

clean:
	rm -rf __pycache__
	rm -rf tests/__pycache__
	rm -rf src/dns/__pycache__
	rm -rf build
	rm -rf dist
	rm -rf dns.egg-info
	rm -rf src/dns.egg-info
	pip uninstall -y dns