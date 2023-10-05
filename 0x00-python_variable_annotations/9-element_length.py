#!/usr/bin/env python3
"""
Module contains element_length function
"""


from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Element lenth
    """
    return [(i, len(i)) for i in lst]
