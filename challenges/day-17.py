from itertools import product
with open('inputs/input-17.txt') as file:
    raw = file.read().splitlines()

def get_adjacent(origin: tuple[int], directions: list, table: set):
    """
    Counts how many cells are alive.
    """
    alive = 0
    for d in directions:
        pos = tuple(origin[i]+d[i] for i in range(len(origin))) # basically 1D matrix addition
        alive += pos in table
    return alive

def conways_iteration(table: set, directions: list):
    """
    Gets all possible cells that can change, then add/remove/keep them.
    Returns the new table.
    """
    old = table.copy() # save the old table for checking
    for pos in product(*[range(min(i)-1,max(i)+2) for i in zip(*old)]): # iterate over all possible cells that can change
        adjacent = get_adjacent(pos,directions,old)
        if pos in old: # add/remove/keep logic
            if adjacent not in (2,3): table.remove(pos)
        else:
            if adjacent == 3: table.add(pos)
    return table

def run(dimensions=3, iterations=6):
    directions = [i for i in product((-1,0,1),repeat=dimensions) if any(i)] # generates all directions for neigbors
    table = set((x,y)+(0,)*(dimensions-2) for x in range(len(raw[0])) for y in range(len(raw)) if raw[x][y]=='#') # generate a set of coordinates that are on
    for _ in range(iterations): # just iterate x amount of times
        table = conways_iteration(table,directions)
    return len(table)

print(run(3,6))
print(run(4,6))
