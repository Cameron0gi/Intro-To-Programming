#!/usr/bin/env python3

i = 0

sum = 0

while i < 5:
    i = i + 1
    x = int(input())
    if (x < 0):
        y = (x * -1)
        sum = sum + y
    else:
        x = x
        sum = sum + x

print(sum)
