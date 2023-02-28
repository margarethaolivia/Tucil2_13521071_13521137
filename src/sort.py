import random
import time

def random_array(size):
    return [round(random.uniform(-1000, 1000), 2) for i in range(size)]

def selection_sort(arr, key):
    for i in range(len(arr)):
        minidx = i
        for j in range(i + 1, len(arr), 1):
            if key(arr[j]) < key(arr[minidx]):
                minidx = j
        tmp = arr[i]
        arr[i] = arr[minidx]
        arr[minidx] = tmp
    return arr

def merge(larr, rarr, key):
    arr = [0 for i in range(len(larr) + len(rarr))]
    lidx = 0
    ridx = 0
    for i in range(len(arr)):
        if lidx == len(larr):
            arr[i] = rarr[ridx]
            ridx += 1
        elif ridx == len(rarr):
            arr[i] = larr[lidx]
            lidx += 1
        elif key(larr[lidx]) < key(rarr[ridx]):
            arr[i] = larr[lidx]
            lidx += 1
        else:
            arr[i] = rarr[ridx]
            ridx += 1
    return arr

def merge_sort(arr, key = lambda x:x):
    """ return arr, sorted using merge sort
    
    """
    if len(arr) <= 43:
        return selection_sort(arr, key)
    mid = len(arr) // 2
    larr = merge_sort(arr[:mid], key)
    rarr = merge_sort(arr[mid:], key)

    return merge(larr, rarr, key)

if __name__ == "__main__":
    print(merge_sort([3, 1, 2, 9, -10.2, 3.4, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3]))

    n = int(input('Ukuran array = '))
    startTime = time.time() * 1000
    r = merge_sort(random_array(n), key=lambda x:-x)
    # random_array(n).sort()
    endTime = time.time() * 1000

    print(r[:20])
    print(f'Waktu Eksekusi     : {endTime - startTime} milisekon')
