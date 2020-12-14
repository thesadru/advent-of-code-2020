with open('inputs/input-14.txt') as file:
    raw = file.read()

data = [] # this could have been a regex, but splitting is more optimized
for part in raw.split('mask = ')[1:]:
    part = part.splitlines()
    mask = part.pop(0)
    mems = []
    for mem in part:
        addr,val = mem.split('] = ')
        mems.append((int(addr[4:]),int(val)))
    data.append((mask,mems))

def mask_val(value: int, mask: str):
    """
    Takes in an integer and a mask. Replaces all specified bits from mask to the integer.
    """
    value = format(value,'36b').replace(' ','0') # pythonic way to turn into bits
    
    masked = ''
    for i,m in enumerate(mask):
        if m=='X':
            masked += value[i]
        else:
            masked += m
    
    return int(masked,2) # get integer from bits

def mask_addr(addr: int, mask: str):
    """
    Takes in an integer and a mask.
    Keeps for all 0s, replaces by 1s.
    For every X, branches into two possibilities of 0/1.
    """
    addr = format(addr,'36b').replace(' ','0') # pythonic way to turn into bits
    
    masked = [''] # keep track of all possible combinations
    for i,m in enumerate(mask):
        if m=='0':
            masked = [a+addr[i] for a in masked] # keep 0s
        elif m=='1':
            masked = [a+'1' for a in masked] # replace with 1s
        else:
            new_masked = [] # branch with Xs (could be one-liner)
            for a in masked:
                new_masked.append(a+'0')
                new_masked.append(a+'1')
            masked = new_masked
    
    return [int(a,2) for a in masked] # convert all addresses into ints

def part1():
    memory = {}
    for mask,mems in data:
        for addr,val in mems:
            memory[addr] = mask_val(val,mask)
    
    return sum(memory.values())

def part2():
    memory = {}
    for mask,mems in data:
        for addr,val in mems:
            for a in mask_addr(addr,mask):
                memory[a] = val
    
    return sum(memory.values())

print(part1())
print(part2())
