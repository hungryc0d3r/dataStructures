# Program for array rotation
# @4l0n3w4rr10r
# method 1
"""
rotate using temp
original array = [1,2,3,4,5], d = 2, n = 5
temp = [1,2], array = [d:] -> [3,4,5] (slicing)
now concat array + temp
"""

import array

arr = array.array('i', [1, 2, 3, 4])
temp = array.array('i', [])
n = len(arr)
d = 2

# temporary array
for i in range(d):
    ad = arr[i]
    temp.append(ad)

# original array
print(f'original array: {arr}')

arr = arr[d:]
rotatedArr = arr+temp
print(f'rotated array: {rotatedArr}')

print('--------------------------------')

# by using function
def rotationArr(Arr, d):
    n = len(Arr)
    temp = array.array('i', [])
    # temporary array
    for i in range(d):
        ad = Arr[i]
        temp.append(ad)

    # original array
    print(f'original array: {Arr}')
    Arr = Arr[d:]
    rotatedArr = Arr + temp
    # result
    print(f'rotated array: {rotatedArr}')

rotationArr(array.array('i', [4,5,6,7,8,9]), 3)
