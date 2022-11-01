#!/usr/bin/env python3

x = int(input())

sum = 0

numbers = [x]

while x != 0:
    x = int(input())

    numbers.append(x)

for x in numbers:
    sum = sum + x

print(sum)
