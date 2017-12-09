import re
with open("day8input.txt") as open_file:
    data = open_file.read().splitlines()

all_registers = {}

highest = 0

for line in data:
    conditional = line.split('if')[1]
    conditional_reg = conditional.split()[0]
    if conditional_reg in all_registers.keys():
        conditional_value = all_registers[conditional_reg]
    else:
        all_registers[conditional_reg]=0
        conditional_value = 0
    final_eval = conditional.replace(str(conditional_reg), str(conditional_value))
    if eval(final_eval):
        instruction = re.search(r'(inc|dec) -?[\d]+' , line).group(0).split()
        multiplier = 1 if instruction[0] == 'inc' else -1
        incrementer = multiplier*int(instruction[1])
        register =  line.split()[0]
        if register in all_registers.keys():
            all_registers[register] += incrementer
        else:
            all_registers[register] = incrementer
        if all_registers[register] > highest:
            highest = all_registers[register]

# part 1
print(max(all_registers.values()))

# part 2
print(highest)