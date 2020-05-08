
from itertools import combinations
import copy
# 1. get all combinations of three points
# 2. list all possible pairs of rectangles
# 3. make all possible rectangles, from three points, with min area
def main():

    N = int(input())
    N_list = []
    for n in range(N):
        n = input()
        n = n.split()
        n = tuple(map(int, n))
        N_list.append(n)

    case1 = 0; case2 = 0; case3 = 0; case4 = 0
    case5 = 0; case6 = 0; case7 = 0; case8 = 0

    C_of_point_coord = list(combinations(N_list, 3))
    point_combination = copy.copy(C_of_point_coord)

    for c in point_combination:
        if (c[0][0] == c[1][0] == c[2][0] or c[0][1] == c[1][1] == c[2][1]):
            C_of_point_coord.remove(c)

    rect_pairs = list(combinations(C_of_point_coord, 2))

    for pair in rect_pairs:
        x_list = []
        y_list = []

        for k in pair[0]:
            x_list.append(k[0])
            y_list.append(k[1])

        x_list1 = []
        y_list1 = []

        for k1 in pair[1]:
            x_list1.append(k1[0])
            y_list1.append(k1[1])

        # 4. compare rectangle positions
        # 5. decide which of the 8 cases they belong
        # 6. count and return the numbers of each case
        # rectangle points (1 and 3) from first_rect list
        p_A1 = (min(x_list), min(y_list))
        p_A3 = (max(x_list), max(y_list))
        # rectangle points (1 and 3) from second_rect list
        p_B1 = (min(x_list1), min(y_list1))
        p_B3 = (max(x_list1), max(y_list1))

        if p_A1 == p_B1 and p_A3 == p_B3:
            case1 = case1 + 1  # case 1
            continue
        if (p_A1[0] <= p_B1[0] and p_B3[0] <= p_A3[0] and p_A1[1] <= p_B1[1] and p_B3[1] <= p_A3[1]) or \
                (p_B1[0] <= p_A1[0] and p_A3[0] <= p_B3[0] and p_B1[1] <= p_A1[1] and p_A3[1] <= p_B3[1]):
            if p_A1[0] == p_B1[0] or p_B3[0] == p_A3[0] or p_A1[1] == p_B1[1] or p_B3[1] == p_A3[1]:
                case3 = case3 + 1  # case 3
                continue
            else:
                case2 = case2 + 1  # case 2
                continue
        else:
            if p_A3[1] < p_B1[1] or p_A3[0] < p_B1[0] or p_B3[1] < p_A1[1] or p_B3[0] < p_A1[0]:
                case4 = case4 + 1  # case 4
                continue
            elif p_A3[1] == p_B1[1] or p_A3[0] == p_B1[0] or p_B3[1] == p_A1[1] or p_B3[0] == p_A1[0]:
                case5 = case5 + 1  # case 5
                continue
            elif ((p_B1[1] < p_A1[1] and p_A3[1] < p_B3[1]) or (p_A1[1] < p_B1[1] and p_B3[1] < p_A3[1])) \
                    and ((p_B1[0] < p_A1[0] and p_A3[0] < p_B3[0]) or (p_A1[0] < p_B1[0] and p_B3[0] < p_A3[0])):
                case8 = case8 + 1  # case 8
                continue
            elif (p_A1[0] <= p_B1[0] and p_B3[0] <= p_A3[0]) or (p_B1[0] <= p_A1[0] and p_A3[0] <= p_B3[0]) \
                    or (p_A1[1] <= p_B1[1] and p_B3[1] <= p_A3[1]) or (p_B1[1] <= p_A1[1] and p_A3[1] <= p_B3[1]):
                case7 = case7 + 1  # case 7
                continue
            else:
                case6 = case6 + 1  # case 6
                continue
    cases = [0, case1, case2, case3, case4, case5, case6, case7, case8]
    for k in range(1, 9):
        print(k, cases[k])

if __name__ == '__main__':
    main()

