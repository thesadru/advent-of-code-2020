with open('inputs/input-08.txt') as file:
    raw = file.read()

instructions = [i.split() for i in raw.splitlines()]


def interpret(instructions):
    """Interprets the instructions, returns accu and if it finished,"""
    hist = set()
    accu = 0
    pointer = 0
    while pointer < len(instructions):
        inst, val = instructions[pointer]
        if inst == 'acc':
            accu += int(val)
            pointer += 1
        elif inst == 'nop':
            pointer += 1
        elif inst == 'jmp':
            pointer += int(val)

        if pointer in hist:
            break
        hist.add(pointer)

    else:
        return accu, True
    return accu, False


def part2():
    for i in range(len(instructions)):
        if instructions[i][0] == 'nop':
            continue # no change, so skip
        
        instructions[i][0] = 'jmp' if instructions[i][0] == 'acc' else 'acc'

        accu, finished = interpret(instructions)
        if finished:
            return accu

        instructions[i][0] = 'jmp' if instructions[i][0] == 'acc' else 'acc'


part1 = interpret(instructions)[0]

print(part1)
print(part2())
