#!/usr/bin/env python3
"""
Module contains measure_runtine function
"""
from time import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension 4x measures the total runtime
    """
    start = time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    end = time()
    return (end - start)
