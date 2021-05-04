import math


def divideChunk(arr, size):

    # final = [arr[i * size:(i + 1) * size]
    #          for i in range((len(arr) + size - 1) // size)]
    # return final

    # looping till length l
    for i in range(0, len(arr), size):
        yield arr[i:i + size]


print(list(divideChunk([1, 2, 3, 4, 5], 2)))
