import time

from sys import stdin
from collections import deque
input = stdin.readline
N = int(input())
K = int(input())
# apple = [[0] * (N+1)] * (N +1)
# for n in range(K):
#     i, j = map(int, input().split())
#     print("apple", apple)
#     apple[i][j] = 1
#     print("i",i)
#     print("j",j)
#     print("apple", apple)
apple = []
for n in range(K):
    apple.append(tuple(map(int, input().split())))
direction_info = int(input())
change_list = deque()
for n in range(direction_info):
    s, d = list(input().split())
    change_list.append((int(s), d))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = 1
start = time.time()

snake = deque()
snake.append((1, 1))
second = 0
while snake:
    # 방향전환
    if change_list:
        if change_list[0][0] == second:
            if change_list[0][1] == "D":
                dir += 1
                if dir == 4:
                    dir = 0
            else:
                dir -= 1
                if dir == -1:
                    dir = 3
            change_list.popleft()
    # 뱀 이동
    next = (snake[-1][0] + dx[dir], snake[-1][1] + dy[dir])
    # 몸통 확인
    if next in snake:
        break
    snake.append(next)
    # 벽 확인
    if snake[-1][0] > N or snake[-1][1] > N or snake[-1][0] < 1 or snake[-1][1] < 1:
        break
    # 사과가 있을 경우
    if snake[-1] in apple:
        apple.remove(snake[-1])
    # 사과가 없을 경우
    else:
        snake.popleft()
    # 시간 경과
    second += 1

print(second + 1)
print(time.time()-start)