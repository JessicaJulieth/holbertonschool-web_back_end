#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay. You will spawn wait_random
    n times with the specified max_delay.
    """

    listdelays = []
    tks = []

    for _ in range(n):
        tks.append(asyncio.create_task(wait_random(max_delay)))
    for t in asyncio.as_completed(tks):
        listdelays.append(await t)

    return listdelays
