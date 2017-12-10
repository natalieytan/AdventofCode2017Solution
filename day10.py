
# Part 1
input= [230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167]
num_list = list(x for x in range(256))
skip_size = 0
position=0
list_size = len(num_list)

for length in input:
    double = num_list*2
    reverse = double[position:position+length][::-1]
    for x in range(length):
        current_pos = (position+x)%list_size
        num_list[current_pos] = reverse[x]
    position+=length+skip_size
    skip_size+=1
    position=(position%list_size)
print(num_list[0]*num_list[1])