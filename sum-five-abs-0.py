#!/usr/bin/env python3

x = int(input())

sum = 0

numbers = [x]

while x != 0:
    x = int(input())
    if (x < 0):
        x = (x * -1)
    else:
        x = x

    numbers.append(x)

for x in numbers:
    sum = sum + x

print(sum)
