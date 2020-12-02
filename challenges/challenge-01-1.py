with open('challenges/input-01.txt') as file:
    raw = file.read()

raw = [int(i) for i in raw.splitlines()]
for i in range(len(raw)):
    for j in range(i+1,len(raw)):
        if raw[i]+raw[j]==2020:
            print(raw[i]*raw[j])
    