with open('input.txt') as fp:
    initial_program = [int(x) for x in fp.read().split(',')]


def run_program(program, noun, verb):
    program[1] = noun
    program[2] = verb
    i = 0
    while i < len(program):
        opcode = program[i]
        if opcode == 99:
            break

        value1 = program[program[i+1]]
        value2 = program[program[i+2]]
        result_position = program[i+3]
        if opcode == 1:
            program[result_position] = value1 + value2
        elif opcode == 2:
            program[result_position] = value1 * value2
        i += 4
    return program[0]


# Part I
print(run_program(initial_program.copy(), 12, 2))


# Part II
for i in range(0, 100):
    for j in range(0, 100):
        val = run_program(initial_program.copy(), i, j)
        if val == 19690720:
            print(i, j)
            print(100 * i + j)
