with open('inputs/input-06.txt') as file:
    raw = file.read()

part1 = 0
part2 = 0
for group in raw.split('\n\n'):
    inter = None
    union = set()
    for answers in group.splitlines():
        union = union.union(answers)
        inter = inter.intersection(answers) if inter is not None else set(answers)

    part1 += len(union)
    part2 += len(inter)

print(part1)
print(part2)
