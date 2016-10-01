#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using for loop function"""

def process_data(data):
    """Returns total sum of data and average of the input data.

    Args:
        data(mixed): a list or tuple of numbers.

    Return:
        tuple: total sum of the data
                average of the data in float

    Examples:
        >>> process_data([1, 2, 3])
        (6, 2.0)

        >>> process_data([2, 3, 4])
        (9, 3.0)
    """
    sumtup = 0
    for mynum in data:
        sumtup += mynum
    avgtup = (sumtup / float(len(data)))
    return (sumtup, avgtup)
