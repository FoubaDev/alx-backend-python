#!/usr/bin/env python3
"""
Python - Async Comprehension.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator function that write a coroutine
    called async_generator that takes no arguments.

    Returns:
        Generator: Asynchronous generator object that can be used in an
        awaitable context.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
