- How to `from dns import *`  when writing test cases:
    - always create a venv via `python -m venv dns`
    - run `source /dns/bin/activate`
    - make sure the `setup.py` is written correctly
    - make sure you have `__init__.py` file
    - run `pip install -e .` 

- after starting the server, run `dig @127.0.0.1 -p 10053 zhenlinw.icu`