#!/usr/bin/env python3
"""
Asunchronious task using ayncio.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns it.
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
