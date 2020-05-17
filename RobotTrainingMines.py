# import time as t
import numpy as np

#
# # input
lenN, rad, sec1, sec2, sec3 = map(int, input().split())
visit_times = np.array(list(map(int, input().split())))
comm = int(input())

# time1 = t.time()


def robot(sec, d, m, x):
    start = sec
    # d - decides which direction left/right to go
    if d == 1:
        sec += m - 1
        if sec >= lenN: sec = lenN - 1
        a = start
        b = sec + 1
    else:
        sec -= m - 1
        if sec < 0: sec = 0
        a = sec
        b = start + 1
    # a, b is distance between start end end point after commend is executed/ robot travels m length on direction d
    # time = sum of all times from a to b
    time = np.sum(visit_times[a:b])

    # here we find influence regions of other two robots, if they are between a, b
    if (a - rad > x[0]) and (x[0] > b + rad):
        section2 = None
    else: section2 = [max(x[0] - rad, a), min(b, x[0] + rad + 1)]

    if (a - rad > x[1]) and (x[1] > b + rad):
        section3 = None
    else: section3 = [max(x[1] - rad, a), min(b, x[1] + rad + 1)]

    # if no robot between a, b we return time
    if section2 is None and section3 is None:
        return time, sec
    # else we find this influenced squares and add to time
    else:
        left = max(section3[0], section2[0])
        right = min(section3[1], section2[1])

        leftm = min(section3[0], section2[0])
        rightm = max(section3[1], section2[1])

        # if they intersect
        if left < right:
            time += np.sum(visit_times[leftm:rightm])
        # if they don't intersect
        else:
            if section2[0] <= section2[1]:
                time += np.sum(visit_times[section2[0]:section2[1]])
            if section3[0] <= section3[1]:
                time += np.sum(visit_times[section3[0]:section3[1]])

    return time, sec


# # output:
total_time = 0

for i in range(comm):
    r, d, m = map(int, input().split())
    # r _ decides which robot we need, x gives location of other robots
    if r == 1:
        x = [sec2, sec3]
        time, sec1 = robot(sec1, d, m, x)
    elif r == 2:
        x = [sec1, sec3]
        time, sec2 = robot(sec2, d, m, x)
    else:
        x = [sec2, sec1]
        time, sec3 = robot(sec3, d, m, x)
    total_time += time

print(total_time)


# time2 = t.time()
# speed = time2 - time1
# print(speed)
