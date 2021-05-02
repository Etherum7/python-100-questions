#  Write a program which takes 2 digits, X,Y as input
#  and generates a 2-dimensional array. The element
# value in the i-th row and j-th column of the array
# should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example
#  Suppose the following inputs are given to the program
# : 3,5 Then, the output of the program should be:
#  [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

numbers = [int(x) for x in input('Enter two numbers ').split(' ')]
arr = [[0 for x in range(numbers[1])] for y in range(numbers[0])]
for i in range(numbers[0]):
    for j in range(numbers[1]):
        arr[i][j] = i*j
print(arr)
