"""
PROBLEM:     000
AUTHOR:      Leon Helwerda
STATUS:      {experimentation, in-progress, needs-optimization, done}
INTERPRETER: Python 2 or 3
EXPLANATION:
    <explanation here>
"""

import timeit

def problem():
    pass

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
