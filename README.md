[![build](https://github.com/criss-wang/DNS_in_Python/workflows/build/badge.svg)](https://github.com/criss-wang/DNS_in_Python/actions?query=workflow%3Abuild)
[![flake8](https://github.com/criss-wang/DNS_in_Python/workflows/lint/badge.svg)](https://github.com/criss-wang/DNS_in_Python/actions?query=workflow%3ALint)
[![license](https://img.shields.io/github/license/criss-wang/DNS_in_Python)](https://github.com/criss-wang/DNS_in_Python/blob/master/LICENSE)  
[![commit](https://img.shields.io/github/last-commit/criss-wang/DNS_in_Python)](https://github.com/criss-wang/DNS_in_Python/commits/master)
[![codecov](https://codecov.io/gh/Criss-Wang/DNS_in_Python/graph/badge.svg?token=STQ529H003)](https://codecov.io/gh/Criss-Wang/DNS_in_Python)
- How to `from dns import *`  when writing test cases:
    - always create a venv via `python -m venv dns`
    - run `source /dns/bin/activate`
    - make sure the `setup.py` is written correctly
    - make sure you have `__init__.py` file
    - run `pip install -e .` 

- after starting the server, run `dig @127.0.0.1 -p 10053 zhenlinw.icu`
