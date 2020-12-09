with open('inputs/input-01.txt') as file:
    raw = file.read()

data = [int(i) for i in raw.splitlines()]


def part1():
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i]+data[j] == 2020:
                return data[i]*data[j]


def part2():
    for i in range(len(data)):
        for j in range(i, len(data)):
            for k in range(j, len(data)):
                if data[i]+data[j]+data[k] == 2020:
                    return data[i]*data[j]*data[k]


print(part1())
print(part2())
