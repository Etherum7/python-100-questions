# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
#  Also please include simple test function to
# test the class methods.

class Play_With_String:
    def __init__(self):
        self.user_string = ''

    def getString(self):
        self.user_string = input('Enter a string ')

    def printString(self):
        print(self.user_string.upper())


user = Play_With_String()
user.getString()
user.printString()
