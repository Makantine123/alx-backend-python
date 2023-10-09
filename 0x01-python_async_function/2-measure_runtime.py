#!/usr/bin/env python3
"""
Module contains measure_time function
"""

from asyncio import run
from time import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    @n: Times to spawn wait_random
    @max_delay: Input for wait_random
    returns: float
    """
    start = time()
    run(wait_n(n, max_delay))
    end = time()
    total_time = end - start
    return total_time / n
