# Program for array rotation
# @4l0n3w4rr10r
# method 4

"""
Reversal algorithm
arr = [1,2,3,4,5,6,7]

reverse(arr[0...d-1])  [2,1,3,4,5,6,7]
reverse(arr[d....n-1]) [2,1,7,6,5,4,3]
reverse(arr[0...n-1])  [3,4,5,6,7,1,2]
"""
import array

arr = array.array('i', [1,2,3,4,5,6,7,8])
n = len(arr)
d = 2


def reverseArray(arr, begin, end):
    while (begin < end):
        temp = arr[begin]
        arr[begin] = arr[end]
        arr[end] = temp
        begin += 1
        end = end-1

def rotateArr(arr, d):
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)
    
def printArr(arr):
    for i in range(len(arr)):
        print(arr[i], end= " ")
        
rotateArr(arr, d)
printArr(arr)
        