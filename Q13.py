# Write a program that accepts a sentence and
# calculate the number of letters and digits.
# Suppose the following input is supplied to the
# program: hello world! 123 Then, the output should be:
#  LETTERS 10 DIGITS 3

user_input = input('Enter a sentence man ')
# total_int = 0
# total_str = 0

d = {'DIGITS': 0, 'LETTERS': 0}

for letter in user_input:

    if(letter.isdigit()):
        d['DIGITS'] += 1
    if(letter.isalpha()):
        d['LETTERS'] += 1

print(f'LETTERS {d["DIGITS"]} DIGITS {d["LETTERS"]}')

# how to use dictionary usefully