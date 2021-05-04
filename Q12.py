# Question: Write a program, which will find all such
#  numbers between 1000 and 3000 (both included) such
# that each digit of the number is an even number. The
#  numbers obtained should be printed in a comma-separated
# sequence on a single line.

number_evens = []
for num in range(1000, 3000+1):
    identifier = 'all odd'
    stringified_number = str(num)
    for digit in stringified_number:
        if int(digit) % 2 == 0:
            identifier = 'all even'
        elif int(digit) % 2 != 0:
            identifier = 'all odd'
        else:
            pass

    if identifier == 'all even':
        number_evens.append(stringified_number)
print(','.join(number_evens))
# learned how to give variables meaningful name and use else  if elif properly
