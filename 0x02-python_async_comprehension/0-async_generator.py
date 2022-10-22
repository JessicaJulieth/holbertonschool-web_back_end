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
    for i in range(10):
        await asyncio.sleep(1)
        yield 10 * random()
