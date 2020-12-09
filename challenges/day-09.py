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
    goal = part1()
    start, end,  total = 1, 0, 0
    while total != goal:
        end += 1
        total += raw[end]
        while total > goal:
            total -= raw[start]
            start += 1
    
    return min(raw[start:end+1])+max(raw[start:end+1])

print(part1())
print(part2())