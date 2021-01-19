import time
from sys import stdin
import math
input = stdin.readline
s, t = list(map(int, input().split()))
result = ""
num = []
def div(t,s):
  a = t/s
  num.append(s)
  if a%s == 0:
    div(a,s)
  else:
    if a == 1:
        return True
    else:
        num.append(a)
        return True

if s == t:
  print("0")
else:
    div(t,s)
    sc = num.count(s)
    if num[-1] != s:
        2c = math.log2(num[-1])
    


print(result)
# print(time.time()-start)