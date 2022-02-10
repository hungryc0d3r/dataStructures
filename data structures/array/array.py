import array
import numpy

# defining array
# method 1
nparr = numpy.array([1, 7, 9])
print(nparr)
print(type(nparr))
# method 2
# arrayName = array.array(type code for data type, [array,items])
myArr = array.array('i', [1, 2, 3, 4])
print(myArr)
print(type(myArr))


# acessing an element in 1-D array
# indexing starts from 0,1,2,.....
print(myArr[1])

# changing value of array with index
myArr[0] = 5
print(myArr)

# summation of elements in 1-D array

# method 1
print(sum(myArr))

# method 2
def sumArray():
    newArr = array.array('i', [5, 6, 7, 8])
    sum = 0
    for i in range(newArr.itemsize):
        sum = sum + newArr[i]
    return sum

# method 3
def newSum(arr):
    summ = 0
    for i in arr:
        summ = summ + i
    return summ


print(sumArray())
print(newSum(myArr))

# creating 2-D array
arr2D = numpy.array([[1, 2, 3], [4, 5, 6]])
print(arr2D)

# acessing an element in 2-D array
print(arr2D[1][1])
