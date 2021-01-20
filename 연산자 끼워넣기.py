from sys import stdin
from itertools import permutations
from math import inf

input = stdin.readline
N = int(input())
A = list(map(int, input().split()))
pl, mi, mul, div = list(map(int, input().split()))
oper = "+ "*pl + "- "*mi + "* "*mul + "/ "*div
oper = list(permutations(list(oper.split()), N-1))
M = -inf
m = inf

for olist in oper:
  count = 0
  r = A[count]
  for op in olist:
    if  op == "+":
      r += A[count+1]
    elif op == "-":
      r -= A[count+1]
    elif op == "*":
      r *= A[count+1]
    elif op == "/":
      if r < 0:
        r = -r
        r = -int(r // A[count+1])
      else:
        r //= A[count+1]
    count += 1
  M = max(M, r)
  m = min(m, r)

print(M)
print(m)