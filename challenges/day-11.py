from copy import deepcopy
with open('inputs/input-11.txt') as file:
    raw = file.read()

data = [list(i) for i in raw.splitlines()]

directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]


def get_adjacent(row, col, table):
    """
    Gets how many adjacent seats are occupied.
    """
    occupied = 0
    for a,b in directions:
        r,c = row+a,col+b
        if 0 <= r < len(table) and 0 <= c < len(table[0]): # check if not out of bounds
            occupied += table[r][c] == '#'
    
    return occupied


def get_visible(row, col, table):
    """
    Gets how many visible seats are occupied,
    """
    occupied = 0
    for a,b in directions:
        r,c = row+a,col+b
        while 0 <= r < len(table) and 0 <= c < len(table[0]): # cycle until out of bounds
            seat = table[r][c]
            if seat != '.':  # since there's no more floor, just break
                occupied += seat == '#'
                break
            
            r,c = r+a,c+b

    return occupied


def conways_iteration(table, tolerancy=4, use_sight=False):
    """
    Does an iteration of conways game of life directly to the table.
    Returns if there was a change.
    """
    old = deepcopy(table)
    for row in range(len(old)):
        for col, seat in enumerate(old[row]):
            if seat == '.':
                continue
            
            if use_sight:
                occupied =  get_visible(row, col, old)
            else:
                occupied = get_adjacent(row, col, old)

            if seat == 'L' and occupied == 0:
                table[row][col] = '#'
            elif seat == '#' and occupied >= tolerancy:
                table[row][col] = 'L'

    return old == table


def count_occupied(table):
    """
    Counts how many seats are occupied in the table.
    """
    occupied = 0
    for row in range(len(table)):
        for seat in table[row]:
            occupied += seat == '#'
    return occupied


def run(tolerancy=4, use_sight=False):
    """
    Runs until the seats stabilize, then return how many occupied seats there are.
    """
    table = deepcopy(data)
    # just iterate until you're done.
    while conways_iteration(table, tolerancy, use_sight):
        pass
        
    return count_occupied(table)


print(run(4,False))
print(run(5,True))
