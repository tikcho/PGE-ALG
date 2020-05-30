from collections import defaultdict
MN = input().split()
M, N = int(MN[0]), int(MN[1])
matrix = []
for line in range(M):
    row = input().split()
    matrix.append(row)


def horiznotal_line(i, j):
    count = 1
    c = j
    L = matrix[i]
    for k in L[j+1:N]:
        c +=1
        if k == '1' and matrix[i-1][c] == '0' and matrix[i+1][c] == '0':
            count +=1
        elif k == '2' and matrix[i-1][c] == '0' and matrix[i+1][c] == '0' and matrix[i][c+1] == '0':
            count += 1
            return count
        else:
            return None


def vertical_line(i, j):
    count = 1
    for k in range(i+1, M):
        if matrix[k][j] == '1' and matrix[k][j+1] == '0' and matrix[k][j-1] == '0':
            count += 1
        elif matrix[k][j] == '2' and matrix[k][j+1] == '0' and matrix[k][j-1] == '0' and matrix[k+1][j] == '0':
            count += 1
            return count
        else:
            return None


Fishes_Dict = defaultdict(int)
for i in range(1, M-1):
    for j in range(1, N-1):
        if matrix[i][j] == '2':
            if matrix[i-1][j] == '0' and matrix[i][j-1] == '0':
                if matrix[i+1][j] == '0' and matrix[i][j+1] == '1':
                    fish = horiznotal_line(i, j)
                    if fish is not None:
                        Fishes_Dict[fish] +=1
                if matrix[i+1][j] == '1' and matrix[i][j+1] == '0':
                    fish = vertical_line(i, j)
                    if fish is not None:
                        Fishes_Dict[fish] += 1

outPut = []
for l in sorted(Fishes_Dict):
    outPut.append((l, Fishes_Dict[l]))

for s in outPut:
    print(s[0], s[1])
