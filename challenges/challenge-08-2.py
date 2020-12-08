with open('challenges/input-08.txt') as file:
    raw = file.read()

instructions = [i.split() for i in raw.splitlines()]
for i in range(len(instructions)):
    instructions[i][0] = 'nop' if instructions[i][0]=='jmp' else ('jmp' if instructions[i][0]=='nop' else 'acc')
    
    hist = set()
    accu = 0
    pointer = 0
    while pointer<len(instructions):
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
    else:
        print(accu)
        break
    
    instructions[i][0] = 'nop' if instructions[i][0]=='jmp' else ('jmp' if instructions[i][0]=='nop' else 'acc')