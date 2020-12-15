with open('inputs/input-15.txt') as file:
    raw = file.read()

data = [int(i) for i in raw.split(',')]

def play(init: list[int], turns: int):
    """
    Plays the memory game. Needs the init numbers and how many turns to play.
    """
    hist = {k:i+1 for i,k in enumerate(init[:-1])} # number:last_turn (+1 for indexing)
    last = init[-1]
    
    for turn in range(len(init),turns):
        if last in hist:
            current = turn-hist[last]
        else:
            current = 0
        
        hist[last] = turn
        last = current
    
    return last

print(play(data,2020))
print(play(data,30000000))
