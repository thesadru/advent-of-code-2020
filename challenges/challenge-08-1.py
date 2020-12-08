with open('challenges/input-08.txt') as file:
    raw = file.read()

instructions = [i.split() for i in raw.splitlines()]
hist = set()
accu = 0
pointer = 0
while True:
    inst,val = instructions[pointer]
    if inst=='acc':
        accu += int(val)
        pointer += 1
    elif inst=='nop':
        pointer += 1
    elif inst=='jmp':
        pointer += int(val)
    
    if pointer in hist:
        break
    hist.add(pointer)

print(accu)