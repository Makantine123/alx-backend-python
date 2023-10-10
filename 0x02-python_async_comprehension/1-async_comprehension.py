#!/usr/bin/env python3
"""
Module contains coroutine async_comprehension
"""

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """
    Async comprehensions
    """
    return [i async for i in async_generator()]
