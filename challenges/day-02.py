with open('inputs/input-02.txt') as file:
    raw = file.readlines()

part1 = 0
part2 = 0
for line in raw:
    line, char, password = line.split()
    a, b = [int(i) for i in line.split('-')]
    char = char[0]

    part1 += a <= password.count(char) <= b
    part2 += (password[a-1] == char) ^ (password[b-1] == char)

print(part1)
print(part2)
