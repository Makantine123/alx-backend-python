#!/usr/bin/env python3
"""
Module contains coroutine called async_generator
"""
import asyncio
import random


async def async_generator():
    """
    Coroutine loops 10 times, each time asynchronously waits 1 secod,
    then yields a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)