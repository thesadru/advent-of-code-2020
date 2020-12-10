with open('inputs/input-10.txt') as file:
    raw = file.read()

data = [int(i) for i in raw.splitlines()]
data.sort()
data.insert(0, 0) # set start to 0


def part1():
    data.append(data[-1]+3) # add the end
    jolt_dif = [0, 0, 0]
    for i in range(1, len(data)):
        jolt_dif[data[i]-data[i-1]-1] += 1
    return jolt_dif[0]*jolt_dif[2]


def part2():
    paths = [0]*len(data)
    paths[-1] = 1

    for i in range(len(data)-2, -1, -1):  # from lenght of path (excluding start+end) to 0
        paths_number = 0
        for j in range(len(data)):
            if data[j] - data[i] > 3:
                break
            paths_number += paths[j]
        paths[i] = paths_number

    return paths[0]


print(part1())
print(part2())
