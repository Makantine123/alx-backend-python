#!/usr/bin/env python3
"""
Module contains to_kv
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Functions take str v and int or float v and returns a tuple
    """
    return (k, v**2)
