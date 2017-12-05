
with open("day5input.txt") as open_file:
    data = open_file.read().splitlines()

def count_steps(part2, input):
    steps = list(map(int, input))
    goal = len(steps)
    position = 0
    count = 0

    while position < goal:
        instruction = steps[position]
        if part2 and instruction >=3:
            steps[position] -= 1
        else:
            steps[position] += 1
        position += instruction
        count+=1

    return count

print('Part 1 :' + str(count_steps(False, data)))
print('Part 2 :' + str(count_steps(True, data)))
