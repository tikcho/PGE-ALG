
# N - points (0, 1 ... N-1), M - paths
N, M = input().split()
N, M = int(N), int(M)

di = {}
mi = {}
path = 0
paths = []
for p in range(M):
    m = input().split()
    paths.append((int(m[0]), int(m[1])))

lakes, waterfalls, points = [], [], []
for n in range(N):
    points.append(n)

    m = input().split()
    number = int(m[0])
    if m[1] == "L":
        lakes.append(number)
    else:
        waterfalls.append(number)

for i in paths:
    if (i[0] in lakes and i[1] in lakes) or (i[0] in waterfalls and i[1] in waterfalls):
        continue
    else:
        # di.setdefault(i[0], []).append(i[1])
        # di.setdefault(i[1], []).append(i[0])
        if i[0] in lakes:
            mi.setdefault(i[0], []).append(i[1])
            di.setdefault(i[1], []).append(i[0])
        if i[1] in lakes:
            mi.setdefault(i[1], []).append(i[0])
            di.setdefault(i[0], []).append(i[1])


# print(mi)
# print(di)
# L1-W1-L2-W2-L3 --> if L1 == L3 --> path
def ispath(key):
    route = []
    routes = []
    L1 = key
    route.append(L1)
    if mi[L1] is not int:
        for i in mi[L1]:
            route.append(i)
            W1 = i
            if di[W1] is not int:
                for j in di[W1]:
                    if j == L1:
                        continue
                    route.append(j)
                    L2 = j
                    if mi[L2] is not int:
                        for a in mi[L2]:
                            if a == W1:
                                continue
                            route.append(a)
                            W2 = a
                            if di[W2] is not int:
                                if L1 in di[W2]:
                                    routes.append(route)
                                else: route = [key]
                                # for b in di[W2]:
                                #     route.append(b)
                                #     L3 = b
                                #     if L3 == L1:
                                #         routes.append(route)
                                #     else:
                                #         route = [key]
    return len(routes)


for k in mi:
    path += ispath(k)
print(path)

