import random
import math
import time

import matplotlib.pyplot as plt

print("Pencarian Pasangan Titik Terdekat")
n = int(input("Masukkan banyaknya titik : "))
r = int(input("Masukkan dimensi vektor  : "))
print()

points = []

for i in range(n):
    point = []
    for j in range(r):
        x = round(random.uniform(-10**3, 10**3), 3)
        point.append(x)
    points.append(point)

closest = 999 ** 9
p1 = 0
p2 = 0
count = 0

start_time = time.time() * 1000
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
end_time = time.time() * 1000

print(points)
print()
print('Pasangan Terdekat')
print(f'Titik 1 : {points[p1]}')
print(f'Titik 2 : {points[p2]}')
print(f'Jarak   : {round(closest, 3)}')
print(f'Banyak Perhitungan : {count}')
print(f'Waktu Eksekusi     : {end_time - start_time} milisekon')

if r == 3:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for p in points:
        x = p[0]
        y = p[1]
        z = p[2]
        ax.scatter(x, y, z, color='black')
    ax.scatter(points[p1][0], points[p1][1], points[p1][2], color='red')
    ax.scatter(points[p2][0], points[p2][1], points[p2][2], color='red')

    plt.show()
