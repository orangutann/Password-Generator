import string
import random
import time

letters = string.ascii_letters
numbers = string.digits
punctuations = string.punctuation

length = 10


def generator(hasNumbers, hasPunctuation):
    pwd = letters
    output = ''
    if hasNumbers:
        pwd += numbers
    if hasPunctuation:
        pwd += punctuations
    for i in range(length):
        test = random.choice(pwd)
        output += test
    return output

n = 10000
t0 = time.time()
for i in range(n): generator(True, True)
t1 = time.time()
total = t1 - t0
print(total) 

print(generator(False, False))
