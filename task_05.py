#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task 05"""

def flip_keys(to_flip):
    """Revers the order of the inner sequence.

    Args:
        to_flip(list): It has a nested and immutable sequences

    Returns:
        list: The original list with its inner elements reversed

    Example:
        >>> LIST = [(1, 2, 3), 'abc']
        >>> NEW = flip_keys(LIST)
        >>> LIST is NEW
        True
        >>> print LIST
        [(3, 2, 1), 'cba']
    """
    mynum = 0
    for myseq in to_flip:
        myseq = to_flip[mynum][::-1]
        to_flip[mynum] = myseq
        mynum += 1
    return to_flip
