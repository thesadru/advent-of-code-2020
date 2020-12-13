import math
with open('inputs/input-13.txt') as file:
    raw = file.read()

raw_time,raw_data = raw.splitlines()
time = int(raw_time)
data = [int(i) for i in raw_data.split(',') if i != 'x']

def part1():
    earliest = math.inf,None
    for n in data:
        bus_time = math.ceil(time/n)*n - time
        if bus_time < earliest[0]:
            earliest = bus_time,n
    
    return earliest[0]*earliest[1]


print(part1())
