#!/usr/bin/env python3

x = input()
y = input()
z = input()

if ((len(x) > len(y)) and (len(x) > len(z))):
    print(x)

elif ((len(y) > len(x)) and (len(y) > len(z))):
    print(y)

else:
    print(z)
