from numba import jit

import random
import time

def get_heads(n: int) -> list:
    ls = []
    for i in range(n):
        if random.random() < 0.5: ls.append(i)
    return ls

""" RUNTIME TEST WITHOUT NUMBA  -------------------------- """

_start_time = time.time()
vals = get_heads(10000000)
_end_time = time.time()

print(str(_end_time - _start_time))

""" RUNTIME TEST WITH NUMBA ------------------------------ """

_start_time = time.time()
jit_get_heads = jit(nopython=True)(get_heads)
vals = jit_get_heads(10000000)
_end_time = time.time()

print(str(_end_time-_start_time))

_start_time = time.time()
vals = jit_get_heads(10000000)
_end_time = time.time()

print(str(_end_time-_start_time))
