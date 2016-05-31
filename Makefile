.PHONY: test

test: export PYTHONPATH = ./
test:
	pyenv exec py.test "$(TEST_ARGS)"

graph_example: export PYTHONPATH = ./
graph_example:
	pyenv exec python example/budget.py
