from sys import stdin
from math import inf
import time
input = stdin.readline
f, s, g, u,d = map(int, input().split())
start = time.time()
n = inf

if s == g:
  n = 0

elif u != 0 and d != 0:
  for i in range(f//u + 1):
    for j in range(f//d + 1):
      if u*i - d*j == g-s:
        n = min(n, i+j)

elif u == 0 and d != 0:
  for i in range(f//d + 1):
    if d*i == s-g:
      n = min(n, i)

elif d == 0 and u != 0:
  for i in range(f//u + 1):
    if u*i == g-s:
      n = min(n, i)

if n == inf:
  print("use the stairs")
else:
  print(n)
print(time.time()-start)