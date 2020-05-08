import copy
def correctly_drown_rect(M, N, matrix, start):
    flag = 'S'
    x_min = start[0]

    x = x_min
    y_min = start[1]
    y = y_min

    # 1. -----> going right
    while (matrix[y][x] == '1') is True:
        #matrix[y][x] = flag
        if x == N - 1:
            x += 1
            break
        x += 1
    x_max = x -1
    #print(x_max)
    # 2. going down
    if matrix[y][x_max] == matrix[y + 1][x_max]:
        while (matrix[y][x_max] == '1') is True:
            #matrix[y][x_max] = flag
            if y == M - 1:
                y += 1
                break
            y += 1
        #print(y)
        y_max = y -1
       # print(y_max)
        # 3. going left    <-----
        if matrix[y_max][x - 1] == matrix[y_max][x - 2]:
            while (matrix[y_max][x - 1] == '1') is True:
                if x == 0:
                    break
                x -= 1
            if x != x_min:
                return None

            # 4. going up
            if matrix[y_max][x_min] == matrix[y_max - 1][x_min]:
                while (matrix[y - 1][x_min] == '1') is True:
                    if y == 0:
                        break
                    y -= 1
                if y == y_min:
                    cell = (x_max - x_min - 1) * (y_max - y_min - 1)
                    return cell

            else:
                return None
        else:
            return None
    else:
        return None

def main():
    # M = column/vertical line;  N = row/horizontal line
    M_N = input().split()
    M = int(M_N[0])
    N = int(M_N[1])

    matrix = []
    for i in range(M):
        row = input().split()
        matrix.append(row)

    num = 0   #! number of correctly drown rectangles
    area = 0   #! the sum of areas of interiors of all correctly drawn retangles

    flag = 'S'
    flagged_start = []

    for y in range(M-1):
        for x in range(N-1):
            # 1. -----> got first corner
            if matrix[y][x] == '1' and matrix[y][x] == matrix[y][x + 1] == matrix[y + 1][x]:
                #x_min = x; y_min = y
                #matrix[y][x] = flag
                flagged_start.append((x, y))
   # print(flagged_start)
    for i in flagged_start:
        ans = correctly_drown_rect(M, N, matrix, i)
        if ans is not None:
            num += 1  # we get +1 rect
            area = area + ans  # area of interior, we need to add them
    print(str(num) + " " + str(area))
    return str(num) + " " + str(area)

main()
