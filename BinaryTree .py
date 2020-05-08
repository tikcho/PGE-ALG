import time
import collections

line_input = input()
list_input = list(map(int,line_input.split()))
AL, AR, C0, CL, CR, D, M, RK, RSR = list_input

# start = time.time()


def keys_cost(k):
    val = k[0]*(k[2]+1)
    return val


def disbalances(sl, sr):
    disbalance = abs(sl-sr)
    return disbalance


def left(data, key):
    dl = (data * AL) % M  # data_left
    kl = (AL * (key + 1)) % M  # key_left
    return dl, kl


def right(data, key):
    dr = (data * AR) % M  # data_right
    kr = (AR * (key + 2)) % M  # data_right
    return dr, kr


def parity_siblings(a, b):
    if a % 2 == b % 2:
        return 1
    else:
        return 0


def keys_sum(vals):
    x = vals[0]
    vmax = min(vals)
    if x > vmax: x = 0
    return x


def maxpath(list):
    path = []
    mpath = 0
    val = [list[0]]
    n = len(list)
    for i in range(1, n):
        if list[i] >= list[i-1]:
            val += [list[i]]
        if list[i] < list[i-1] or i == n-1:
            if len(val) > 1:
                path.append(sum(val))
                val = [list[i]]
            else: val = [list[i]]
    if path != []:
        mpath = max(path)
    return mpath


def dfs(stack):
    tree, leafs, st, depthdic = {}, [], [stack[0][0]], {}
    parity, indx, val = 0, 0, 0
    subtrees, values, rr = [], [], []

    while stack != []:
        [key, data, depth] = stack.pop()
        subtrees.append([key, data, depth])
        indx += 1
        depthdic.setdefault(depth, []).append(indx)

        if depth != D and C0 <= data:

            data_left, key_left = left(data, key)
            data_right, key_right = right(data, key)
            cdepth = depth + 1

            if data < CL:
                tree[indx] = [key, key_left, None]
                st = st + [key_left]
                stack.append([key_left, data_left, cdepth])
                continue

            if CL <= data < CR:
                tree[indx] = [key, None, key_right]
                st = st + [key_right]
                stack.append([key_right, data_right, cdepth])
                continue

            if CR <= data < M:
                tree[indx] = [key, key_left, key_right]
                rr.append(st + [key_right])
                st = st + [key_left]
                stack.append([key_right, data_right, cdepth])
                stack.append([key_left, data_left, cdepth])

                p = parity_siblings(key_left, key_right)
                parity = parity + p  # ---> 4.

        else:
            tree[indx] = [key, None, None]
            leafs.append(key)
            val = maxpath(st)
            values.append(val)

            if rr != []:
                st = rr.pop()
            else:
                st = []

    return tree, leafs, parity, values, subtrees, depthdic


def main():
    de = collections.deque()
    d2 = collections.deque()
    lmin = collections.deque()
    maxv = collections.deque()
    ltrees = collections.deque()
    mpath, disbal, balance2 = 0, 0, 0
    wdom, L1 = 0, 0
    minkeys = []

    stack = [[RK, RSR, 0]]
    tree, leafs, parity, maxvalues, subtrees, depthdic = dfs(stack)

    if maxvalues != []:
        mpath = max(maxvalues)
    cost = sum(list(map(keys_cost, subtrees)))
    deep = list(depthdic)
    deep.reverse()

    for i in deep[1:]:
        if i == deep[1]:
            for j in depthdic[i]:  # for each line, for each node j
                key, Lkey, Rkey = tree[j]
                if (Lkey is None) and (Rkey is None):
                    de.append(key)
                    d2.append(0)
                    lmin.append([key])
                    maxv.append(key)
                    ltrees.append(0)
                    continue
                else:
                    if Lkey is None and Rkey is not None:
                        disbal += Rkey
                        de.append(key + Rkey)
                        d2.append(0)
                        m = [key, Rkey]
                        localmin = keys_sum(m)
                        minkeys.append(localmin)
                        lmin.append(m)
                        if key >= Rkey:
                            wdom += 1
                        maxv.append(Rkey)
                        ltrees.append(None)

                    if Rkey is None and Lkey is not None:
                        disbal += Lkey
                        de.append(key + Lkey)
                        d2.append(0)
                        m = [key, Lkey]
                        localmin = keys_sum(m)
                        minkeys.append(localmin)
                        lmin.append(m)
                        if key >= Lkey:
                            wdom += 1
                        maxv.append(Lkey)
                        L1 +=1
                        ltrees.append(1)

                    if Lkey is not None and Rkey is not None:
                        disbal += abs(Lkey - Rkey)
                        de.append(key + Lkey + Rkey)
                        d2.append(1)
                        balance2 += key
                        m = [key, Rkey, Lkey]
                        localmin = keys_sum(m)
                        minkeys.append(localmin)
                        lmin.append(m)
                        if key >= Lkey and key >= Rkey:
                            wdom += 1
                        maxv.append(max(Lkey, Rkey))
                        ltrees.append(0)
            continue

        for n in depthdic[i]:  # for each line, for each node j
            key, Lkey, Rkey = tree[n]
            if (Lkey is None) and (Rkey is None):
                de.append(key)
                d2.append(0)
                lmin.append([key])
                maxv.append(key)
                ltrees.append(0)
                continue
            else:
                if Lkey is None and Rkey is not None:
                    Rkey = de.popleft()
                    disbal += Rkey
                    de.append(key + Rkey)
                    v = d2.popleft()
                    d2.append(v)
                    l = lmin.popleft()
                    m = [key] + l
                    localmin = keys_sum(m)
                    minkeys.append(localmin)
                    lmin.append(m)
                    lf = maxv.popleft()
                    if key >= lf:
                        wdom += 1
                    maxv.append(lf)
                    ltrees.popleft()
                    ltrees.append(None)

                if Rkey is None and Lkey is not None:
                    Lkey = de.popleft()
                    disbal += Lkey
                    de.append(key + Lkey)
                    v = d2.popleft()
                    d2.append(v)
                    l = lmin.popleft()
                    m = [key] + l
                    localmin = keys_sum(m)
                    minkeys.append(localmin)
                    lmin.append(m)
                    lf = maxv.popleft()
                    if key >= lf:
                        wdom += 1
                    maxv.append(lf)
                    lt = ltrees.popleft()
                    if lt is not None:
                        L1 += 1
                        ltrees.append(1)
                    else: ltrees.append(None)

                if Lkey is not None and Rkey is not None:
                    Lkey = de.popleft()
                    Rkey = de.popleft()
                    disbal += abs(Lkey - Rkey)
                    de.append(key + Lkey + Rkey)

                    v1 = d2.popleft()
                    v2 = d2.popleft()
                    if v1 == v2: balance2 += key
                    d2.append(v1 + v2 + 1)

                    l = lmin.popleft()
                    l2 = lmin.popleft()
                    m = [key] + l + l2
                    localmin = keys_sum(m)
                    minkeys.append(localmin)
                    lmin.append(m)

                    lf = maxv.popleft()
                    lf2 = maxv.popleft()
                    if key >= lf and key >= lf2:
                        wdom += 1
                    maxv.append(max(lf, lf2))

                    lt = ltrees.popleft()
                    lt2 = ltrees.popleft()
                    if lt is None or lt2 is None:
                        ltrees.append(None)
                    if lt is not None and lt2 is not None:
                        if (lt + lt2) > 0:
                            L1 += 1
                            ltrees.append(1)
                        else: ltrees.append(0)

    #output:
    print(cost)
    print(disbal)
    print(balance2 + sum(leafs))
    print(parity)
    print(sum(minkeys) + sum(leafs))
    print(wdom)
    print(L1)
    print(mpath)


main()

# end = time.time()
# print(end - start)


