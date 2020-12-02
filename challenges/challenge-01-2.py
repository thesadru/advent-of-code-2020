with open('challenges/input-01.txt') as file:
    raw = file.read()

raw = [int(i) for i in raw.splitlines()]
for i in range(len(raw)):
    for j in range(i,len(raw)):
        for k in range(j,len(raw)):
            if raw[i]+raw[j]+raw[k]==2020:
                print(raw[i]*raw[j]*raw[k])
    