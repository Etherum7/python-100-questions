# Question: Write a program that computes the net amount
#  of a bank account based a transaction log from console
# input. The transaction log format is shown as following:
#  D 100 W 200

# D means deposit while W means withdrawal. Suppose the
# following input is supplied to the program:
# D 300 D 300 W 200 D 100 Then, the output should be: 500

def divideChunk(arr, size):

    # final = [arr[i * size:(i + 1) * size]
    #          for i in range((len(arr) + size - 1) // size)]
    # return final

    # looping till length l
    for i in range(0, len(arr), size):
        yield arr[i:i + size]


transaction_log = input('Enter transactions to know balance ').split(' ')
formatted_transactions = divideChunk(transaction_log, 2)
balance = 0
for transaction in formatted_transactions:
    if transaction[0].lower() == 'd':
        balance += int(transaction[1])
    if transaction[0].lower() == 'w':
        balance -= int(transaction[1])
print(f'Your balance is {balance}')



