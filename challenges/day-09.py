from itertools import combinations
with open('inputs/input-09.txt') as file:
    raw = file.read()

raw = [int(i) for i in raw.splitlines()]
valsize = 25

def part1():
    validation,data = raw[:valsize],raw[valsize:]
    while len(data)>0:
        n = data.pop(0)
        if not any(i+j==n and i!=j for i,j in combinations(validation,2)):
            return n
        
        validation.append(n)
        validation.pop(0)

def part2():
    n = part1()
    chunksize = 1
    while True:
        for i in range(len(raw)-chunksize):
            s = sum(raw[i:i+chunksize])
            if s==n:
                return max(raw[i:i+chunksize])+min(raw[i:i+chunksize])
            elif s>n:
                break # optimization
        
        chunksize += 1

print(part1())
print(part2())