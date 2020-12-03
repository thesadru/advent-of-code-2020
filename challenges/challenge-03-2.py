with open('challenges/input-03.txt') as file:
    raw = file.readlines()

total = 1
for c,r in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    trees = 0
    row,col = 0,0
    while row<len(raw):
        trees += raw[row][col % 31]=='#'
        row += r
        col += c
    total *= trees
print(total)