import random
import math


def genOTP():
    digits = [i for i in range(0, 10)]
    random_str = ''

    for i in range(6):
        index = math.floor(random.random() * 10)
        random_str += str(digits[index])
    # print(random_str)

    return random_str
