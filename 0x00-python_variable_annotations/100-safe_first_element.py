#!/usr/bin/env python3
"""
Module contain safe_first_elements function with duck-typed annotations
"""


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function
    """
    if lst:
        return lst[0]
    else:
        return None
