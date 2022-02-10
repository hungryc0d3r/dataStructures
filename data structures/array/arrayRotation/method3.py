# Program for array rotation
# @4l0n3w4rr10r
# method 3
"""
Juggling method
"""
import array
import math

arr = array.array('i', [1, 2, 3, 4, 5, 6, 7])
n = len(arr)
d = 2

def rotate(Arr, d, n):
    d = d % n
    GCD = math.gcd(n, d)  # no of iterations
    for i in range(GCD):
        temp = arr[i]     # storing temp values
        j = i
        while 1:
            k = j + d     
            # if k >= n
            if k >= n:
                k = k - n
            # breaking loop
            if k == i:
                break
            arr[j] = arr[k]   # 0 = 2, 2 = 4, 4 = 6
            j = k
        arr[j] = temp

# for printing the array
def printArray(arr, size):
    for i in range(size):
        print("% d" % arr[i], end=" ")


rotate(arr, d, n)
printArray(arr, n)
