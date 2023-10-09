#!/usr/bin/env python3
"""
Module contains wait_n function
"""

import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: float) -> List[float]:
    """
    @n: Times to spawn wait_random
    @max_delay: Input for wait_random
    """
    myWaits = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*myWaits)
    return sorted(results)
