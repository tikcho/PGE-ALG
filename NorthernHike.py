from timeit import default_timer as timer

min_distance, max_distance, min_time, max_time, min_elevation, max_elevation = map(int, input().split())
hike_min_distance, hike_max_distance, hike_min_elevation, hike_max_elevation = map(int, input().split())
N = int(input())
start = timer()


class Checkpoint:
    def __init__(self, c, e, d, t, diff):
        self.elevation = e
        self.distance = d
        self.time = t
        self.camp = c
        self.diff = diff

    def __str__(self):
        return "Test a:% s b:% s b:% s" % (self.distance, self.time, self.diff)


def new_camps(prev_camp, points, i):
    for j in range(prev_camp + 1, i):
        points[prev_camp].distance = points[prev_camp].distance + points[j].distance
        points[prev_camp].time = points[prev_camp].time + points[j].time
        points[prev_camp].diff = points[prev_camp].diff + points[j].diff
    return [points[prev_camp].distance, points[prev_camp].time, points[prev_camp].diff]


def better_hike(hike, best_hike):
    if hike[0] > best_hike[0]:
        best_hike = hike
    elif hike[0] == best_hike[0] and hike[1] > best_hike[1]:
        best_hike = hike
    elif hike[0] == best_hike[0] and hike[1] == best_hike[1] and hike[2] < best_hike[2]:
        best_hike = hike
    return list(best_hike)


def sectionsSubArr(arr, arr2, arr3):
    begin, end = 0, 0
    currSum, currElev, currTime = arr[0], arr2[0], arr3[0]
    distances, elevations, sections, endPs = {}, {}, {}, {}

    while end < len(arr):
        if currSum <= max_distance and currElev <= max_elevation and currTime <= max_time:
            if currSum >= min_distance and currElev >= min_elevation and currTime >= min_time:
                distances[begin] = currSum
                elevations[begin] = currElev
                endPs[begin] = end

        if currSum < max_distance and currElev <= max_elevation and currTime < max_time:
            end += 1
            if end < len(arr):
                currSum += arr[end]
                currElev += arr2[end]
                currTime += arr3[end]
        else:
            if currSum - arr[end] >= min_distance and currElev - arr2[end] >= min_elevation and currTime - arr3[end] >= min_time:
                w1, w2 = currSum - arr[end], currElev - arr2[end]
                distances[begin] = w1
                elevations[begin] = w2
                endPs[begin] = end

            currSum -= arr[begin]
            currElev -= arr2[begin]
            currTime -= arr3[begin]
            begin += 1
    # print(begin, end)
    while begin < end-1:
        currSum -= arr[begin]
        currElev -= arr2[begin]
        currTime -= arr3[begin]
        begin += 1
        if currSum <= max_distance and currElev <= max_elevation and currTime <= max_time:
            if currSum >= min_distance and currElev >= min_elevation and currTime >= min_time:
                distances[begin] = currSum
                elevations[begin] = currElev
                endPs[begin] = end
    return distances, elevations, endPs





# # - - - - - - - - - - - - - # # - - - - - - - - - - - - - # # - - - - - - - - - - - - -
# # - - - - - - - - - - - - - - - M A I N    C O D E - - - - - - - - - - - - - - - - - # #
# # - - - - - - - - # # - - - - - - - - - - - - - - - # # - - - - - - - - - - - - - - - -


points, camps = [], []
dD, eE, tT,  = [], [], []
# best_hike = [0, 0, 0]
for i in range(N):
    C, E, D, T = map(int, input().split())
    diff = 0
    x = Checkpoint(C, E, D, T, diff)
    points.append(x)

    if i > 0:
        elev1 = points[i - 1].elevation
        if E > elev1:
            diff = E - elev1

    points[i - 1].diff = diff
    if C == 1:
        if camps:
            prev_camp = camps[-1]
            p = new_camps(prev_camp, points, i)
            dD.append(p[0])
            eE.append(p[2])
            tT.append(p[1])
        camps.append(i)

dD.append(0)
eE.append(0)
tT.append(0)

dist, elev, graph = sectionsSubArr(dD, eE, tT)
key = list(graph.keys())
key.reverse()
arr = key.copy()
# print(graph)
# print(key)
# print(dD)
# print(eE)

sps = set(arr)

# hike_list = []
best_hike = [0, 0, 0]
tot_dist, tot_elev, tot_sec = 0, 0, 0
while arr:
    sp = arr.pop()
    if sp not in sps:
        if tot_dist >= hike_min_distance and tot_elev >= hike_min_elevation:
            # hike_list.append([tot_dist, tot_elev, tot_sec])
            hike = [tot_dist, tot_elev, tot_sec]
            best_hike = better_hike(hike, best_hike)
            tot_dist, tot_elev, tot_sec = 0, 0, 0
            continue
        else: continue
    ep = graph[sp]
    if tot_dist + dist[sp] == 82518:
        print((sp, ep))

    if tot_dist + dist[sp] <= hike_max_distance and tot_elev + elev[sp]<= hike_max_elevation:
        tot_dist += dist[sp]
        tot_elev += elev[sp]
        tot_sec += 1
        arr.append(ep)
    else:
        if tot_dist >= hike_min_distance and tot_elev >= hike_min_elevation:
            # hike_list.append([tot_dist, tot_elev, tot_sec])
            hike = [tot_dist, tot_elev, tot_sec]
            best_hike = better_hike(hike, best_hike)
        tot_dist, tot_elev, tot_sec = 0, 0, 0
        # arr.pop()
    # if sp == 17088: print(sp, ep, tot_dist, tot_elev, tot_sec, graph[ep], dist[ep])

if tot_dist <= hike_max_distance and tot_elev <= hike_max_elevation and tot_dist >= hike_min_distance and tot_elev >= hike_min_elevation:
    # hike_list.append([tot_dist, tot_elev, tot_sec])
    hike = [tot_dist, tot_elev, tot_sec]
    best_hike = better_hike(hike, best_hike)
# hike_list.sort()
# best_hike = hike_list[-1]

#
# print(hike_list)
print(best_hike[0], best_hike[1], best_hike[2])



end = timer()
print(end - start)


