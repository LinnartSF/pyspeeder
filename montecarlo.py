import numpy as np
from matplotlib import pyplot as plt
import random
import time
from numba import njit

def random_walker(n: int, length: int) -> np.ndarray:

    arr = np.zeros((n, length), dtype = float)

    for i in range(n):

        idx = 100

        for j in range(length):
            
            idx += idx*random.gauss(0.00015, 0.02)

            arr[i, j] = idx
    
    return arr

@njit
def nb_random_walker(n: int, length: int) -> np.ndarray:

    arr = np.zeros((n, length), dtype = float)

    for i in range(n):

        idx = 100

        for j in range(length):
            
            idx += idx*random.gauss(0.00015, 0.02)

            arr[i, j] = idx
    
    return arr

# --- monte carlo run without numba ------------------
starttime = time.time()
arr = random_walker(10000, 365)
endtime = time.time()

print("monte carlo random walk without NUMBA; 1st time: ")
print(endtime-starttime)

starttime = time.time()
arr = random_walker(10000, 365)
endtime = time.time()

print("monte carlo random walk without NUMBA; 2nd time: ")
print(endtime-starttime)

# --- monte carlo run with numba --------------------
starttime = time.time()
arr = nb_random_walker(10000, 365)
endtime = time.time()

print("monte carlo random walk with NUMBA; 1st time: ")
print(endtime-starttime)

starttime = time.time()
arr = nb_random_walker(10000, 365)
endtime = time.time()

print("monte carlo random walk with NUMBA; 2nd time: ")
print(endtime-starttime)

starttime = time.time()
arr = nb_random_walker(10000, 365)
endtime = time.time()

print("monte carlo random walk with NUMBA; 3nd time: ")
print(endtime-starttime)

# --- lets see the random walk simulation ----------

plt.figure()
for i in range(10000):
    plt.plot(range(1,366),arr[i,], alpha=0.01,color = "red", linewidth=1)
plt.xlabel("simulation time")
plt.ylabel("price index")
plt.title("Price index over time")
plt.show()

# --- now repeat the monte carlo simulaiton 100 times and remember the reduction in runtime thanks to numba ----

savings = np.zeros(50, dtype = float)

for i in range(50):
    mark = time.time()
    arr = random_walker(10000,365)
    diff1 = time.time() - mark
    mark = time.time()
    arr = nb_random_walker(10000,365)
    diff2 = time.time() - mark
    savings[i] = diff1/diff2

plt.figure()
plt.hist(savings)
plt.show()







