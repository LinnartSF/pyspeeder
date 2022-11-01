import numpy as np

from numba import jit, njit, vectorize

import random
import time

def rand_events(n: int) -> np.ndarray:
    ls = np.zeros(n)
    for i in range(n):
        x = random.random()
        while True:
            y = random.random()
            if x < y: 
                ls[i] = y
                break
    return ls

""" RUNTIME TEST WITHOUT NUMBA  -------------------------- """

_start_time = time.time()
vals = rand_events(10000000)
_end_time = time.time()

print(str(_end_time - _start_time))

""" RUNTIME TEST WITH NUMBA ------------------------------ """

_start_time = time.time()
jit_rand_events = jit(nopython=True)(rand_events)
vals = jit_rand_events(10000000)
_end_time = time.time()

print(str(_end_time-_start_time))

_start_time = time.time()
vals = jit_rand_events(10000000)
_end_time = time.time()

print(str(_end_time-_start_time))
