"""
Package setup script for Euler modules.
"""

from pathlib import Path
from setuptools import setup, find_packages
from Euler import __version__

_directory = Path(__file__).parent.resolve()

setup(name='Euler',
      version=__version__,
      description='Modules implementing algorithms for number theory and '
                  'other mathematics, with potential use for Project Euler or '
                  'Advent of Code',
      long_description=(_directory / 'README.md').read_text(encoding='utf-8'),
      long_description_content_type='text/markdown',
      url='https://github.com/lhelwerd/euler',
      author='Leon Helwerda',
      author_email='l.s.helwerda@liacs.leidenuniv.nl',
      license='MIT',
      packages=find_packages(),
      package_data={'Euler': ['py.typed']},
      include_package_data=True,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12',
          'Topic :: Scientific/Engineering :: Mathematics'
      ],
      keywords=[
          'number theory', 'mathematics', 'algorithms', 'formulas', 'primality',
          'divisors', 'palindromes', 'roman', 'triangles'
      ],
      install_requires=['numpy', 'sortedcontainers'],
      python_requires='>=3.8'
)
