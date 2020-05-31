
# Python3
from math import gcd
a, b = [int(i) for i in input().split()]


def getLCM(a, b):
    return int(a * b / gcd(a, b))

print(getLCM(a,b))