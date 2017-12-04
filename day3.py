def distance(num):
    nearest_root = int(num ** 0.5)
    if nearest_root % 2 == 0:
        shell_size = (nearest_root + 1)
    else:
        shell_size = nearest_root + 2

    last_square = (shell_size-2)**2
    difference = num - last_square
    shell_minus = shell_size - 1 
    corners_and_square = []
    for i in range(5):
        corners_and_square.append(last_square + i*shell_minus)
    half_shell = shell_size//2

    def get_distance(corner):
        a_distance = (half_shell)
        b_distance = abs(((shell_size-2)//2) - (num - corner-1))
        return a_distance + b_distance

    if num == last_square:
        distance = shell_size - 2
    elif difference % (shell_size -1) == 0:
        distance = shell_size - 1
    else:
        for i in range(1,5):
            if num < corners_and_square[i]:
                distance = get_distance(corners_and_square[i-1])
                break
    return distance

print(distance(265149))
