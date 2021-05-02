# Question: Write a program that calculates and prints
# the value according to the given formula: Q = Square
# root of [(2 * C * D)/H] Following are the fixed values
# of C and H: C is 50. H is 30. D is the variable whose
# values should be input to your program in a
# comma-separated sequence. Example Let us assume the
# following comma separated input sequence is given to
#  the program: 100,150,180 The output of the program
# should be: 18,22,24
import math

C, H = 50, 30
# def calc_area():
#     C, H = 50, 30
#     arr = input('Enput numbers seperated by commas ').split(',')

#     for num in arr:
#         print(round(((2*C*int(num))/H)**0.5))


# calc_area()

items = [int(x)
         for x in input('Enput numbers seperated by commas ').split(',')]
values = []

for d in items:
    values.append(str(round(math.sqrt((2*C*d)/H))))
print(','.join(values))
