with open('inputs/input-05.txt') as file:
    raw = file.read().splitlines()


def to_int(seat):
    return int(seat.translate(str.maketrans('BFRL', '1010')), 2)


def part1():
    highest = 0
    for seat in raw:
        highest = max(highest, to_int(seat))
    return highest


def part2():
    seatids = set()
    for seat in raw:
        seatids.add(to_int(seat))

    for i in range(len(raw)):
        if i not in seatids and i+1 in seatids and i-1 in seatids:
            return i


print(part1())
print(part2())
