with open('inputs/input-03.txt') as file:
    raw = file.readlines()


def part1(c=3, r=1):
    trees = 0
    row, col = 0, 0
    while row < len(raw):
        trees += raw[row][col % 31] == '#'
        row += r
        col += c
    return trees


def part2():
    total = 1
    for c, r in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        total *= part1(c, r)
    return total


print(part1())
print(part2())
