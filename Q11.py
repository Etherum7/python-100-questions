# Write a program which accepts a sequence of comma
# separated 4 digit binary numbers as its input and
# then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed
# in a comma separated sequence. Example:
# 0100,0011,1010,1001 Then the output should be: 1010
#  Notes: Assume the data is input by console.
user_numbers = [x for x in input(
    'Enter numbers separated by comma ').split(',')]

divisible_by_five = []

for bin_num in user_numbers:
    if int(bin_num, 2) % 5 == 0:
        divisible_by_five.append(bin_num)
print(','.join(divisible_by_five))

# learned that int accepts string when converting