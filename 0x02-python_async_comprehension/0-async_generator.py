#!/usr/bin/env python3

"""
Async Generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """
    Coroutine called async_generator that takes no arguments
    """
    for _ in range(10):
        await asyncio.sleep(1)
        r = random.uniform(0, 10)
        yield
