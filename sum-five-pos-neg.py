#!/usr/bin/env python3

i = 0

num = [x]

num_neg = [y]

x = int(input())

while x != 0:
    if (x < 0):
        y = (x)
    else:
        x = x

    num.append(x)
    num_neg.append(y)


print(num_neg, num)
