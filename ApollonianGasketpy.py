import math
# input --> D1 D2 minD
# output --> L1 L2
# L1 --> sum of Areas
# L2 --> sum of perimeters

def circle_k(k1, k2, k3, minR):
    K = []
    k4 = abs(k1 + k2 + k3 + 2 * (k1*k2+k2*k3+k3*k1)**(1/2))
    r = 1 / k4
    d = 2 * r
    if minR <= r:
        K.append(d)
        K = K + circle_k(k4, k2, k3, minR)
        K = K + circle_k(k4, k1, k2, minR)
        K = K + circle_k(k4, k1, k3, minR)
        return K
    else:
        return K

def main():
    input_numbers = input(' ').split()
    D1 = float(input_numbers[0]); r1 = D1/2; k1 = 1/r1
    D2 = float(input_numbers[1]); r2 = D2/2; k2 = 1/r2
    minD = float(input_numbers[2]); minR = minD/2
    k3 = -1 / (r1 + r2)

    area = (math.pi * r1 ** 2) + (math.pi * (r2 ** 2))
    perimeter = (math.pi * D1 + math.pi * D2)

    K = circle_k(k1, k2, k3, minR)
    for d in K:
        area += 0.5 * math.pi * (d ** 2)
        perimeter += 2 * math.pi * d

    L1 = format(area, '.3f')
    L2 = format(perimeter, '.3f')
    print(L1, L2)


main()
