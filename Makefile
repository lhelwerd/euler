COVERAGE=coverage
MYPY=mypy
ifeq (,$(shell which uv))
	PIP=python -m pip
else
	PIP=uv pip
endif
PYLINT=pylint
PYRIGHT=basedpyright
RUFF=ruff check
RM=rm -rf
SOURCES=Euler
TESTS=tests
TEST=-m unittest discover -s $(TESTS)

.PHONY: all
all: coverage mypy pylint

.PHONY: release
release: test mypy pylint clean build tag push upload

.PHONY: setup
setup:
	$(PIP) install .

.PHONY: setup_release
setup_release:
	$(PIP) install . --group release

.PHONY: setup_analysis
setup_analysis:
	$(PIP) install . --group analysis

.PHONY: setup_test
setup_test:
	$(PIP) install . --group test

.PHONY: install
install: setup

.PHONY: pylint
pylint:
	$(PYLINT) $(SOURCES) $(TESTS)

.PHONY: ruff
ruff:
	$(RUFF) $(SOURCES) #$(TESTS)

.PHONY: mypy
mypy:
	$(MYPY) $(SOURCES) $(TESTS) \
		--html-report mypy-report \
		--cobertura-xml-report mypy-report \
		--junit-xml mypy-report/TEST-junit.xml \
		--no-incremental --show-traceback

.PHONY: pyright
pyright:
	$(PYRIGHT) $(SOURCES) #$(TESTS)

.PHONY: test
test:
	python $(TEST)

.PHONY: coverage
coverage:
	$(COVERAGE) run --source=$(SOURCES) $(TEST)
	$(COVERAGE) report -m
	$(COVERAGE) xml -i -o test-reports/cobertura.xml

.PHONY: build
build:
	python -m build

.PHONY: clean
clean:
	# Unit tests and coverage
	$(RM) .coverage htmlcov/ test-reports/
	# Typing coverage and Pylint
	$(RM) .mypy_cache mypy-report/ pylint-report.txt
	# Pip and distribution
	$(RM) src/ build/ dist/ Euler.egg-info/
