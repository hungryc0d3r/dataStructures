# Program for array rotation
# @4l0n3w4rr10r
# method 2
"""
rotate one by one
"""
import array
arr = array.array('i', [1,2,3,4,5,6,7])
n = len(arr)

def arrayRotation(Arr, d, n):
    for i in range(d):
        rotateOnebyOne(Arr, n)


def rotateOnebyOne(Arr, n):
    temp = Arr[0]
    for i in range(n-1):
        Arr[i] = Arr[i+1]
    Arr[n-1] = temp

def printArr(size):
    for i in range(7):
        print(arr[i] , end= " ")
        
arrayRotation(arr, 2, 7)
printArr(7)

print("")
print("--------------------------")

# using function
def Result(Oarr, d):
    n = len(Oarr)
    def arrayRotation(Oarr, d):
        for i in range(d):
            rotateOnebyOne(Oarr)


    def rotateOnebyOne(Oarr):
        temp = Oarr[0]
        for i in range(n-1):
            Oarr[i] = Oarr[i+1]
        Oarr[n-1] = temp

    def printArr():
        for i in range(n):
            print(Oarr[i] , end= " ")    

    arrayRotation(Oarr, d)
    printArr()

Result(array.array('i', [1,2,3,4,5,6,7,8]), 2)