#!/usr/bin/env python3
"""
Module contains make_multiplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function takes multiplier and returns function
    that multiplies a float by multiplier
    """
    return lambda x: x * multiplier
