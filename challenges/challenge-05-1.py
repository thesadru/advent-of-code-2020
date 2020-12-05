with open('challenges/input-05.txt') as file:
    raw = file.read().splitlines()

highest = 0
for seat in raw:
    seatid = int(seat.translate(str.maketrans('BFRL','1010')),2)
    highest = max(highest,seatid)
print(highest)
