#!/usr/bin/env python3

x  = int(input())

if (x >= 2) and ((x // 1) == x) and ((x // x) == 1):
    print("prime")

else:
    print("not prime")
