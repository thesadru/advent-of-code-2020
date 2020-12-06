with open('challenges/input-06.txt') as file:
    raw = file.read()

total = 0
for group in raw.split('\n\n'):
    inter = None
    for answers in group.splitlines():
        if inter is not None:
            inter &= set(answers)
        else:
            inter = set(answers)
    total += len(inter)
print(total)