#!/usr/bin/env python3
"""
Module contains sum_mixed_list function
"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Function recieves list of integers and returns a float
    """
    return float(sum(mxd_list))
