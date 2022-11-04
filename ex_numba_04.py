import numpy as np

from numba import jit, njit

import random
import time

# agent class, representing agents in agent-based model
class Agent:

    attribute1: float
    attribute2: float

    def __init__(self, val1: float, val2: float):
        self.attribute1 = val1
        self.attribute2 = val2

# implement the agent-based simulation grid
grid_agent = [[None for i in range(100)] for j in range(100)]  # grid contains None or agent instance references (custom datatype)
grid_id = [[0 for i in range(100)] for j in range(100)]        # grid will only contain integers, either 0 or the id of an agent

# populate the grid with some agents and maintain the IDs in a dictionary

agentdict = {}
id = 0

for i in range(100):
    for j in range(100):
        if random.random() < 0.5: 
            id += 1
            agent = Agent(random.random(), random.random())
            grid_agent[i][j] = agent
            grid_id[i][j] = id
            agentdict[id] = agent

# --- NEIGHBOURHOOD SEARCH WITHOUT NUMBA -------------------------

def search_neighbourhood(row: int, col: int, radius: int, grid: list, iterations: int) -> None:

    row_min = row-radius
    row_max = row+radius
    col_min = col-radius
    col_max = col+radius

    returnls = []

    for _ in range(iterations): # adding iterations just to consume more time to see impact of numba later

        returnls = []

        if row_min < 1: row_min = 1
        if row_max > 100: row_max = 100
        if col_min < 1: col_min = 1
        if col_max > 100: col_max = 100

        for i in range(row_min,row_max+1):
            for j in range(col_min,col_max+1):
                if i == row and col == col:
                    pass
                elif grid[i-1][j-1]:
                    returnls.append(grid[i-1][j-1])
    
    # return last list of references
    return returnls


starttime = time.time()
returnls = search_neighbourhood(50,50,20,grid_agent,100000)
endtime = time.time()
#print("neighbours: "+str(returnls))
print("time consumed: "+str(endtime-starttime))

# --- NEIGHBOURHOOD SEARCH WITH NUMBA ----------------------

@jit
def search_neighbourhood_jitted(row: int, col: int, radius: int, grid: list, iterations: int) -> None:

    row_min = row-radius
    row_max = row+radius
    col_min = col-radius
    col_max = col+radius

    returnls = np.zeros(100,100)

    for _ in range(iterations): # adding iterations just to consume more time to see impact of numba later

        returnls = np.zeros(100,100)

        if row_min < 1: row_min = 1
        if row_max > 100: row_max = 100
        if col_min < 1: col_min = 1
        if col_max > 100: col_max = 100

        for i in range(row_min,row_max+1):
            for j in range(col_min,col_max+1):
                if i == row and col == col:
                    pass
                elif grid[i-1][j-1] > 0:
                    returnls[i,j] = grid[i-1][j-1]
    
    # return last list of references
    return returnls[:1]

starttime = time.time()
returnls = search_neighbourhood_jitted(50,50,20,grid_id,100000)
endtime = time.time()
#print("neighbours: "+str(returnls))
print("time consumed: "+str(endtime-starttime))


