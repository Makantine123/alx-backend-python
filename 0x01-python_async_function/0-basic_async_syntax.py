#!/usr/bin/env python3
"""
Module contains wait_random function
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Takes intenger max_delay with a default value 10
    Function randomly waits between 0 and max_delay
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
