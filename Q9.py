# Write a program that accepts sequence of lines as
#  input and prints the lines after making all
#  characters in the sentence capitalized. Suppose
#  the following input is supplied to the program:
# Hello world Practice makes perfect Then, the output
#  should be: HELLO WORLD PRACTICE MAKES PERFECT
arr = []
while True:
    user_input = input('Enter a string to be capitalized ')
    if user_input:
        arr.append(user_input.upper())
    else:
        break


print('\n'.join(arr))
