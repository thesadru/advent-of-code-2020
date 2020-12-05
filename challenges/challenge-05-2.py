with open('challenges/input-05.txt') as file:
    raw = file.read().splitlines()

seatids = set()
for seat in raw:
    seatids.add(int(seat.translate(str.maketrans('BFRL','1010')),2))

for i in range(len(seatids)):
    if i not in seatids and i+1 in seatids and i-1 in seatids:
        print(i)
