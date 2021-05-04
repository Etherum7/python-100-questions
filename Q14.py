# Write a program that accepts a sentence and
#  calculate the number of upper case letters
# and lower case letters. Suppose the following
#  input is supplied to the program: Hello world!
# Then, the output should be: UPPER CASE 1 LOWER CASE 9

cases = {'uppercase': 0, 'lowercase': 1}

user_input = input('Enter a sentence ')

for letter in user_input:
    if(letter.isupper()):
        cases['uppercase'] += 1
    elif(letter.islower()):
        cases['lowercase'] += 1
    else:
        pass
print(f'UPPER CASE {cases["uppercase"]} LOWER CASE {cases["lowercase"]}')
