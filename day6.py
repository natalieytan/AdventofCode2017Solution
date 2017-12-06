def find_steps(block_init, all_blocks):
    all_blocks = []
    blocks = block_init[:]

    while blocks not in all_blocks:
        all_blocks.append(blocks[:])
        highest = max(blocks)
        position = blocks.index(highest)
        blocks[position] = 0
        floor = highest//len(blocks)
        remainder =  highest%len(blocks)
        while remainder:
            if (position) == len(blocks)-1:
                position = 0
            else:
                position +=1
            blocks[position] += 1
            remainder -=1
        blocks = [x+floor for x in blocks]

    part1 = len(all_blocks)
    part2 = len(all_blocks) - (all_blocks).index(blocks)

    return (part1, part2)



print(find_steps([4,1,15,12,0,9,9,5,5,8,7,3,14,5,12,3], []))

