#!/usr/bin/env python3
"""Tasks
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function (do not create an async function, use the regular
       function syntax to do this) task_wait_random that takes an
       integer max_delay and returns a asyncio.Task.
    """
    random = []
    for _ in range(n):
        random.append(await task_wait_random(max_delay))
    return sorted(random)
