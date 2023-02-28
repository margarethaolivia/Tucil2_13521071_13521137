import random
import time
import matplotlib.pyplot as plt

import dnc
import bf


# generate random points and add it into a list
def generatePoints(n, r):
    points = []
    p = []
    for i in range(n):
        point = []
        for j in range(r):
            x = round(random.uniform(-10**3, 10**3), 3)
            point.append(x)
        t = (i, point)
        points.append(point)
        p.append(t)
    return points, p


# print a point
def printPoint(point):
    print('(', end='')
    for i in range(len(point)-1):
        print(point[i], end=', ')
    print(point[r-1], end=')\n')


# display gui for 3D points visualization
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

# dimension input validation
while (r < 2):
    print('Masukan tidak valid!')
    r = int(input("Masukkan dimensi vektor  : "))
print()

# generate n points
points, p = generatePoints(n, r)
print(f'MEMBANGKITKAN {n} TITIK ACAK')
for point in points:
    printPoint(point)

print()
print('Memproses dengan algoritma Brute Force...')
print()

# Brute Force algorithm
startTime = time.time() * 1000
closest, p1, p2, count = bf.bruteForce(n, r, points)
endTime = time.time() * 1000

# Brute Force statistics
print('ALGORITMA BRUTEFORCE')
print(f'Titik 1 : ', end='')
printPoint(points[p1])
print(f'Titik 2 : ', end='')
printPoint(points[p2])
print(f'Jarak   : {round(closest, 3)}')
print(f'Banyak Perhitungan : {count}')
print(f'Waktu Eksekusi     : {endTime - startTime} milisekon')

print()
print('Memproses dengan algoritma Divide and Conquer...')
print()

# DnC algorithm
startTime = time.time() * 1000
closest, p1, p2, count = dnc.getClosestPair(p)
endTime = time.time() * 1000

# DnC statistics
print('ALGORITMA DIVIDE AND CONQUER')
print(f'Titik 1 : ', end='')
printPoint(points[p1])
print(f'Titik 2 : ', end='')
printPoint(points[p2])
print(f'Jarak   : {round(closest, 3)}')
print(f'Banyak Perhitungan : {count}')
print(f'Waktu Eksekusi     : {endTime - startTime} milisekon')

# ask for visualization (3D only)
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
