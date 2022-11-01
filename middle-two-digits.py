#!/usr/bin/env python3

x = int(input())

c = (((x // 1000) % 10) * 10)

d = (x // 100) % 10

print(c + d)
