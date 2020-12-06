with open('challenges/input-06.txt') as file:
    raw = file.read()

total = 0
for group in raw.split('\n\n'):
    union = set()
    for answers in group.splitlines():
        union |= set(answers)
    total += len(union)
print(total)