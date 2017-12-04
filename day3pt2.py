def check_around(x, y, matrix):
    value = 0
    for i in range (x-1, x+2):
        for j in range (y-1, y+2):
            if (i, j) in matrix:
                value += matrix[(i, j)]
    matrix[(x,y)] = value
    return matrix

def go_right(x, y, matrix):
    x += 1
    matrix = check_around(x, y, matrix)
    return x, y, matrix

def go_left(x, y, matrix):
    x -= 1
    matrix = check_around(x, y, matrix)
    return x, y, matrix

def go_down(x, y, matrix):
    y -= 1
    matrix = check_around(x, y, matrix)
    return x, y, matrix

def go_up(x, y, matrix):
    y += 1
    matrix = check_around(x, y, matrix)
    return x, y, matrix

def move_one(x, y, matrix):
    if abs(x) == abs(y):
        if x > 0 and y > 0:
            x, y, matrix = go_left(x, y, matrix)
        elif x < 0 and y > 0:
            x, y, matrix = go_down(x, y, matrix)
        elif (x <= 0 and y <= 0) or (x > 0 and y < 0):
            x, y, matrix = go_right(x, y, matrix)
    elif (x > 0) and (abs(y) < abs(x)):
        x, y, matrix = go_up(x, y, matrix)
    elif (y > 0) and (abs(x) < abs(y)):
        x, y, matrix = go_left(x, y, matrix)
    elif (x < 0) and (abs(y) < abs(x)):
        x, y, matrix = go_down(x, y, matrix)
    elif (y < 0) and (abs(x) < abs(y)):
        x, y, matrix = go_right(x, y, matrix)
    
    return x, y, matrix

def spiral(x, y, matrix, goal):  
    x, y, matrix = move_one(x, y, matrix)
    current = matrix[(x, y)]
    if current < goal:
        return spiral(x, y, matrix, goal)
    else:
        return current



print(spiral(0, 0, {(0, 0) : 1,} , 265149))
