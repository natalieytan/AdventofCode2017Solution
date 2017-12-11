# part 2
# Used numpy to reduce bitwise operations
# To select what needed to be reversed, I doubled the original array for easier selection
# To loop through the array & insert reverse string, I used modulus
import numpy as np

num_list = list(x for x in range(256))
skip_size = 0
position=0
list_size = len(num_list)
ascii_input = list(ord(str(x)) for x in str('AoC 2017'))
ascii_input.extend([17, 31, 73, 47, 23])

for _ in range(64):
    for length in ascii_input:
        double = num_list*2
        reverse = double[position:position+length][::-1]
        for x in range(length):
            current_pos = (position+x)%list_size
            num_list[current_pos] = reverse[x]
        position+=length+skip_size
        skip_size+=1
        position=(position%list_size)
hex_list = []
for i in range(0, 256, 16):
    hex_list.append(hex(np.bitwise_xor.reduce(num_list[i:i+16]))[2:])
answer = ''.join(hex_list )
print('Part 2', answer)