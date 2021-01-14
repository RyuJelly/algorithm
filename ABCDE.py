import time
from sys import stdin
from collections import deque
input = stdin.readline
N, M = list(map(int, input().split()))
relation = [[] for i in range(N)]
visited = [False] * N
for i in range(M):
    n, m = list(map(int, input().split()))
    relation[n].append(m)
    relation[m].append(n)

start = time.time()
friends = []
def ABCDE(start):
    print("여기1")
    friends.append(start)
    for n in relation[start]:
        if not visited[n]:            
            visited[start] = True
            print("여기2")
            ABCDE(n)
        else:
            print("여기3")
            continue
ABCDE(0)
print(relation)
print(visited.count(True))
print(visited)
print(friends)
print(time.time()-start)