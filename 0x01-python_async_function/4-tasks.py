#!/usr/bin/env python3
"""
Module contains wait_n function
"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    @n: Times to spawn wait_random
    @max_delay: Input for wait_random
    """
    myWaits: asyncio.Task = [task_wait_random(max_delay) for _ in range(n)]
    results: List[float] = await asyncio.gather(*myWaits)
    return sorted(results)
