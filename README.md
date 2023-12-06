# Euler

This repository contains some Python modules that implement algorithms for 
number theory and other fields of mathematics, but also some file processing 
methods. Potential applications that these modules could be used for are 
[Project Euler](https://projecteuler.net/) problems and [Advent of 
Code](https://adventofcode.com/) puzzles.

The modules are written for Python 3.8+. Support for older versions is dropped 
in version 0.0.2. The oldest versions of the modules support running on older 
versions as well, which are from back when [PyPy](https://www.pypy.org/) was 
only starting to support Python 3 code.

## Installation

Source releases of versions are available from 
[GitHub](https://github.com/lhelwerd/euler/tags).

When using the source release or if this repository is cloned, then 
installation of the module is possible with:

```
pip install -r requirements.txt
python setup.py build
python setup.py install
```

To install a development version of the modules as a dependency, use 
`git+https://github.com/lhelwerd/euler.git@main#egg=Euler` in 
a `requirements.txt` or similar. Other syntax exists to mark dependency for 
a specific release, see [requirements file 
format](https://pip.pypa.io/en/stable/reference/requirements-file-format/) for 
inspiration.

## License

The Euler module is licensed under the MIT License. See the [LICENSE](LICENSE) 
file for more information.
