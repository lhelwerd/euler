# Euler

[![coverage](https://github.com/lhelwerd/euler/actions/workflows/coverage.yml/badge.svg)](https://github.com/lhelwerd/euler/actions/workflows/coverage.yml)
[![Coverage Status](https://coveralls.io/repos/github/lhelwerd/euler/badge.svg?branch=main)](https://coveralls.io/github/lhelwerd/euler?branch=main)

This repository contains some Python modules that implement algorithms for 
number theory and other fields of mathematics, but also some file processing 
methods. Potential applications that these modules could be used for are 
[Project Euler](https://projecteuler.net/) problems and [Advent of 
Code](https://adventofcode.com/) puzzles.

The modules are written for Python 3.9+ and for PyPy 3.10+. Support for 
versions before 3.8 is dropped in version 0.0.2 and support for 3.8 is dropped 
in version 0.0.3. The modules support running on [PyPy](https://www.pypy.org/) 
(currently those based on Python 3.10) as well. Detailed information on changes 
for each version is found in the [changelog](CHANGELOG.md) file.

## Installation

Source releases of versions are available from 
[GitHub](https://github.com/lhelwerd/euler/tags).

When using the source release or if this repository is cloned, then 
installation of the module is possible with `pip install` followed by either 
the release zip/tarball or the current directory. `make install` installs from 
the current directory. We recommend using virtual environments to keep your 
dependencies separate from global installation.

To install a development version of the modules as a dependency, use 
`git+https://github.com/lhelwerd/euler.git@main#egg=Euler` in 
a `requirements.txt` or similar. Other syntax exists to mark dependency for 
a specific release, see [requirements file 
format](https://pip.pypa.io/en/stable/reference/requirements-file-format/) for 
inspiration.

## Testing

In the repository, run unit tests using `make test`. Additionally, obtain 
coverage information by first installing dependencies with `make setup_test`. 
Then, use `make coverage` to perform the unit tests and receive output in the 
form of a textual report and XML report. Finally, you could use `coverage html` 
to receive a HTML report.

Typing and style checks are also possible by first installing dependencies 
using `make setup_analysis`. Then, use `make mypy` to run the type checker and 
receive HTML and XML reports. Style checks are done by using `make pylint` for 
an aggregate report output.

## License

The Euler module is licensed under the MIT License. See the [license](LICENSE) 
file for more information.
