import random
import math
import time

import matplotlib.pyplot as plt


def generatePoints(n, r):
    points = []
    for i in range(n):
        point = []
        for j in range(r):
            x = round(random.uniform(-10**3, 10**3), 3)
            point.append(x)
        points.append(point)
    return points


def printPoint(point):
    print('(', end='')
    for i in range(len(point)-1):
        print(point[i], end=', ')
    print(point[r-1], end=')\n')


def printVisualization(points, p1, p2):
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


print("        PENCARIAN PASANGAN TITIK TERDEKAT          ")
print("===================================================")
n = int(input("Masukkan banyaknya titik : "))
r = int(input("Masukkan dimensi vektor  : "))
print()

points = generatePoints(n, r)

closest = 999 ** 9
p1 = 0
p2 = 0
count = 0

print()
print('Memproses...')
print()

# Brute Force
startTime = time.time() * 1000
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
endTime = time.time() * 1000

print(f'MEMBANGKITKAN {n} TITIK ACAK')
for point in points:
    printPoint(point)

print()
print('ALGORITMA BRUTEFORCE')
print(f'Titik 1 : ', end='')
printPoint(points[p1])
print(f'Titik 2 : ', end='')
printPoint(points[p2])
print(f'Jarak   : {round(closest, 3)}')
print(f'Banyak Perhitungan : {count}')
print(f'Waktu Eksekusi     : {endTime - startTime} milisekon')

print()
print('ALGORITMA DIVIDE AND CONQUER')
# algo divide and conquer

if r == 3:
    print()
    show = input('Ingin menampilkan visualisasi? [Y/n] : ').lower()
    while (show != 'y' and show != 'n'):
        print('Masukan tidak valid!')
        show = input('Ingin menampilkan visualisasi? [Y/n] : ').lower()

    if (show == 'y'):
        print('Menampilkan visualisasi...')
        printVisualization(points, p1, p2)

print('===================================================')
print('    TERIMA KASIH TELAH MENGGUNAKAN PROGRAM KAMI    ')
