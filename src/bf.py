import math


def bruteForce(n, r, points):
    closest = 999 ** 9
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            distance = 0
            for k in range(r):
                distance += (points[i][k] - points[j][k]) ** 2
            distance = math.sqrt(distance)
            count += 1
            if distance < closest:
                closest = distance
                p1 = i
                p2 = j
    return closest, p1, p2, count
