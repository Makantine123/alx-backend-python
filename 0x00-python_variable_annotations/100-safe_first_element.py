#!/usr/bin/env python3
"""
Module contain safe_first_elements function with duck-typed annotations
"""


from types import NoneType
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """
    Function
    """
    if lst:
        return lst[0]
    else:
        return None
