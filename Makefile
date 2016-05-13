.PHONY: test

test: export PYTHONPATH = ./
test:
	pyenv exec py.test
