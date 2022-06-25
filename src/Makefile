.PHONY: test

default: test

test:
	PYTHONPATH=. pytest -s

test-filter:
	PYTHONPATH=. pytest -s -k $(FILTER)