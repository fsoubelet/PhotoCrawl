# Copyright 2019 Felix Soubelet <felix.soubelet@cern.ch>
# MIT License

# Documentation for most of what you will see here can be found at the following links:
# for the GNU make special targets: https://www.gnu.org/software/make/manual/html_node/Special-Targets.html
# for python packaging: https://docs.python.org/3/distutils/introduction.html

# ANSI escape sequences for bold, cyan, dark blue, end, pink and red.
B = \033[1m
C = \033[96m
D = \033[34m
E = \033[0m
P = \033[95m
R = \033[31m

.PHONY : help archive checklist clean condaenv docker-build docker-pull format install lines lint reinstall uninstall tests

all: install

help:
	@echo "Please use 'make $(R)<target>$(E)' where $(R)<target>$(E) is one of:"
	@echo "  $(R) archive $(E)        to create a tarball of this specific release."
	@echo "  $(R) checklist $(E)      to print a pre-release check-list."
	@echo "  $(R) clean $(E)          to recursively remove build, run, and bitecode files/dirs."
	@echo "  $(R) format $(E)         to recursively apply PEP8 formatting through the 'Black' cli tool."
	@echo "  $(R) install $(E)        to 'pip install' this package into your current (virtual) environment."
	@echo "  $(R) lines $(E)          to count lines of code with the 'tokei' tool."
	@echo "  $(R) lint $(E)           to lint your python code though 'PyLint'."
	@echo "  $(R) reinstall $(E)      to 'pip uninstall' then 'pip install' this package into your current (virtual) environment."
	@echo "  $(R) uninstall $(E)      to uninstall the 'pyhdtoolkit' package from your activated environment."

archive:
	@echo "$(B)Creating tarball archive of this release.$(E)"
	@echo ""
	@python setup.py sdist
	@echo ""
	@echo "$(B)Your archive is in the $(C)dist/$(E) $(B)directory. Link it to your release.$(E)"
	@echo "To install from this archive, unpack it and run '$(D)python setup.py install$(E)' from within its directory."
	@echo ""

checklist:
	@echo "Here is a small pre-release check-list:"
	@echo "  - Check you are on a tagged $(P)feature/release$(E) branch (see Gitflow workflow)."
	@echo "  - Check you have updated the version number of $(C)__version__.py$(E) according to semantic versioning."
	@echo "  - Check the $(P)feature/release$(E) branch tag matches this release's package version."
	@echo "  - After merging and pushing this release from $(P)master$(E) to $(P)origin/master$(E):"
	@echo "     - Run 'make $(R)archive$(E)'."
	@echo "     - Create a Github release and attach the created tarball to it."
	@echo "     - Run 'make $(R)clean$(E)'."

clean:
	@echo "Running setup clean."
	@python setup.py clean
	@echo "Cleaning up distutils remains."
	@rm -rf build
	@rm -rf dist
	@rm -rf pyhdtoolkit.egg-info
	@rm -rf .eggs
	@echo "Cleaning up bitecode files and python cache."
	@find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	@echo "Cleaning up pytest cache."
	@find . -type d -name '*.pytest_cache'  -exec rm -rf {} + -o -type f -name '*.pytest_cache' -exec rm -rf {} +
	@echo "All cleaned up!\n"

format:
	@echo "Formatting code to PEP8, default line length is 120."
	@black -l 120 .

install: format clean
	@echo "Installing this package to your active environment."
	@pip install .

lines: format
	@tokei .

lint: format
	@echo "Linting code, ignoring the following message IDs:"
	@echo "  - $(P)C0330$(E) $(C)'bad-continuation'$(E) since it somehow doesn't play friendly with $(D)Black$(E)."
	@echo "  - $(P)W0106$(E) $(C)'expression-not-assigned'$(E) since it triggers on class attribute reassignment."
	@echo "  - $(P)E0401$(E) $(C)'import error'$(E) because PyLint is confused with the conda environments."
	@echo "  - $(P)W1202$(E) $(C)'logging-format-interpolation'$(E) because on this, PyLint is full of shit.\n"
	@pylint --max-line-length=120 --disable=C0330,W0106,C0103,W1202,R0903,E0401 pyhdtoolkit/

reinstall: uninstall install

uninstall:
	@echo "Uninstalling this package from your active environment."
	@pip uninstall photocrawl --yes

.DEFAULT:
	@echo "Make caught an invalid target! See help output below for available targets."
	@make help
