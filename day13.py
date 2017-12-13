with open("day13input.txt") as open_file:
    data = open_file.read().strip().splitlines()

scanners = {}
for line in data:
    scan_depth = int(line.split(':')[0])
    scan_range = int(line.split(':')[1].strip())
    scanners[scan_depth] = scan_range

# part 1
penalty = 0
for scan_depth, scan_range in scanners.items():
    if not scan_depth%(2*(scan_range-1)):
        penalty +=scan_depth*scan_range
print('part 1 penalty:', penalty)

# part 2
delay=0
caught = True
while caught:
    penalty = 0 
    for scan_depth, scan_range in scanners.items():
        if not (delay+scan_depth)%(2*(scan_range-1)):
            penalty +=1
            break
    if penalty:
        delay+=1
    else:
        print('part 2 delay: ', delay)
        caught = False