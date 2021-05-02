# Question: Write a program which can compute the factorial
#  of a given numbers. The results should be printed in a
#  comma-separated sequence on a single line. Suppose the
#  following input is supplied to the program: 8 Then, the
#  output should be: 40320

def compute_factorial(number):
    factorial = 1
    for i in range(1, number+1):
        factorial *= i
    return factorial


arr = input(
    'Enter numbers seperated by space of which fibonacci is to be calcuted? ').split(' ')
for num in arr:
    print(compute_factorial(int(num)))
