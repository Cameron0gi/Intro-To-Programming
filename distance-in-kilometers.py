#!/usr/bin/env python3

x = int(input())

a = x % 10

b = (((x // 10) % 10) * 100)

c = (((x // 100) % 10) * 10)

d = ((x // 1000) % 10)

y = x // 1000

if(b + c + d) < 500:
  z = 0  
else:
  z = 1 


print(y + z)