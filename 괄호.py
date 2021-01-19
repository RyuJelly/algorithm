import time
from sys import stdin
input = stdin.readline
T = int(input())
VPS_list = [input().split() for _ in range(T)]

for i in VPS_list:
    YorN = True
    r = 0
    l = 0
    if i[0].count('(') == i[0].count(')'):
        for j in i[0]:
            if j == "(":
                l += 1
            else:
                r += 1
            if r > l:
                print("NO")
                YorN = False
                break
        if YorN:
            print("YES")
    else:
        print("NO")
# print(time.time()-start)