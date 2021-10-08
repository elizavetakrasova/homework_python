import random
import string
n = int(input())

def gen(n):
    s=''
    for i in range(n):
        s=s + random.choice(string.ascii_letters)
    return s

print(gen(n))




