import random

def generateBadPoints(n, r):
    points = []
    p = []
    for i in range(n):
        point = [i % 3, 0, i // 3]
        for j in range(3, r, 1):
            x = round(random.uniform(-10**3, 10**3), 3)
            point.append(x)
        t = (i, point)
        points.append(point)
        p.append(t)
    return points, p