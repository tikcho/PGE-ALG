NM = input().split()
N, M = int(NM[1]), int(NM[0])
dict = {}

matrX = []
for i in range(M):
    row = input().split()
    matrX.append(row)


def cooperation(y, x, dict):
    R = matrX[y][x]
    degree = 0
    # y line:
    if y == 0:
        for i1 in range(1, M):
            if matrX[i1][x] == '2':
                break
            if matrX[i1][x] == '1':
                degree += 1
                dict.setdefault((x, y), []).append((x, i1))
                break
    if y == M:
        for i2 in range(M - 1, -1, -1):
            if matrX[i2][x] == '2':
                break
            if matrX[i2][x] == '1':
                degree += 1
                dict.setdefault((x, y), []).append((x, i2))
                break
    if y != 0 and y != M:
        for i3 in range(y + 1, M):
            if matrX[i3][x] == '2':
                break
            if matrX[i3][x] == '1':
                degree += 1
                dict.setdefault((x, y), []).append((x, i3))
                break
        for i4 in range(y - 1, -1, -1):
            if matrX[i4][x] == '2':
                break
            if matrX[i4][x] == '1':
                degree += 1
                dict.setdefault((x, y), []).append((x, i4))
                break
    # now x line:
    if x == 0:
        for j1 in range(1, N):
            if matrX[y][j1] == '2':
                break
            if matrX[y][j1] == '1':
                degree += 1
                dict.setdefault((x, y), []).append((j1, y))
                break
    if x == N:
        for j2 in range(N - 1, -1, -1):
            if matrX[y][j2] == '2':
                break
            if matrX[y][j2] == '1':
                degree += 1
                dict.setdefault((x, y), []).append((j2, y))
                break
    if x != 0 and x != N:
        for j3 in range(x + 1, N):
            if matrX[y][j3] == '2':
                break
            if matrX[y][j3] == '1':
                degree += 1
                dict.setdefault((x, y), []).append((j3, y))
                break
        for j4 in range(x - 1, -1, -1):
            if matrX[y][j4] == '2':
                break
            if matrX[y][j4] == '1':
                degree += 1
                dict.setdefault((x, y), []).append((j4, y))
                break
    return degree, dict


mi = {}
for y in range(M):
    for x in range(N):
        R = matrX[y][x]
        if R == '1':
            degree, di = cooperation(y, x, dict)
            mi[(x, y)] = degree

fin = []
for g in dict:
    val = dict[g]
    for h in val:
        R1 = g
        R2 = h
        fin.append(mi[R1] + mi[R2])

r1, r2, r3, r4, r5, r6, r7 = 0, 0, 0, 0, 0, 0, 0
for s in fin:
    if s == 2:
        r1 += 1
    if s == 3:
        r2 += 1
    if s == 4:
        r3 += 1
    if s == 5:
        r4 += 1
    if s == 6:
        r5 += 1
    if s == 7:
        r6 += 1
    if s == 8:
        r7 += 1

k = [r1, r2, r3, r4, r5, r6, r7]

for i in range(2, 9):
    ans = int(k[i - 2])
    print(i, int(ans / 2))