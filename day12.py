import re
with open("day12input.txt") as open_file:
    data = open_file.read().strip().splitlines()

pipe_map = {}
for line in data:
    pipe_map[line.split(' <-> ')[0]] = line.split(' <-> ')[1].split(', ')


def master_pipe(original_pipe):
    pipes_linked = []
    def pipe_linked(original_pipe):
        pipes = pipe_map[original_pipe]
        for pipe in pipes:
            if pipe not in pipes_linked:
                pipes_linked.append(pipe)
                pipe_linked(pipe)
    pipe_linked(original_pipe)
    return pipes_linked

print('part 1:', len(master_pipe('0')))
all_pipes = list(pipe_map.keys())
groups = 0

while all_pipes:
    current_linked = (master_pipe(all_pipes[0]))
    all_pipes = list(set(all_pipes) - set(current_linked))
    groups += 1

print('part 2:', groups)
