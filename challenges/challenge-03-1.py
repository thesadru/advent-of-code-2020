with open('challenges/input-03.txt') as file:
    raw = file.readlines()

trees = 0
for x in range(len(raw)):
    trees += raw[x][x*3 % 31]=='#'
print(trees)