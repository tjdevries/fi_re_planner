.PHONY: test

test: export PYTHONPATH = ./
test:
	pyenv exec py.test "$(TEST_ARGS)"
