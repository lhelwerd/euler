"""
PROBLEM:     019
AUTHOR:      Leon Helwerda
STATUS:      {experimentation, in-progress, needs-optimization, done}
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of Sundays in the 20th century
"""

import timeit

month_days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def problem():
    year = 1900
    # Silly 0-indexers
    month = 1
    wday = 1
    sundays = 0
    while year < 2001:
        wday += month_days[month - 1]
        # February just passed
        if month == 2 and is_leap(year):
            wday += 1
        wday = wday % 7
        sundays += year >= 1901 and wday == 0

        year = year + (month + 1) // 12
        month = (month + 1) % 12

    print(sundays)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

