#!/usr/bin/env python3

x = int(input())

a = x % 10

b = (x // 10) % 10

c = (x // 100) % 10

d = (x // 1000) % 10

e = (x // 10000) % 10

f = (x // 100000) % 10

temp = c

c = d

d = temp

print((c) + (d * 10))
