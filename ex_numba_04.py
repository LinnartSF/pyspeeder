import numpy as np

from numba import njit

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
grid_agent = [[None for i in range(10)] for j in range(10)]  # grid contains None or agent instance references (custom datatype)
grid_id = [[0 for i in range(10)] for j in range(10)]        # grid will only contain integers, either 0 or the id of an agent

# populate the grid with some agents and maintain the IDs in a dictionary

agentdict = {}
id = 0

for i in range(10):
    for j in range(10):
        if random.random() < 0.5: 
            id += 1
            agent = Agent(random.random(), random.random())
            grid_agent[i][j] = agent
            grid_id[i][j] = id
            agentdict[id] = agent

# --- NEIGHBOURHOOD SEARCH WITHOUT NUMBA -------------------------

def get_neighbourhood(row: int, col: int, radius: int, grid: list) -> list:
    row_min = row-radius
    row_max = row+radius
    col_min = col-radius
    col_max = col+radius

    returnls = []

    if row_min < 1: row_min = 1
    if row_max > 10: row_max = 10
    if col_min < 1: col_min = 1
    if col_max > 10: col_max = 10

    for i in range(row_min,row_max+1):
        for j in range(col_min,col_max+1):
            if i == row and col == col:
                pass
            elif grid[i-1][j-1]:
                returnls.append(grid[i-1][j-1])

    returnls

starttime = time.time()
neighbours = get_neighbourhood(5,5,3,grid_agent)
endtime = time.time()
print("neighbours: ")
print(neighbours)
print("time consumed: "+str(endtime-starttime))