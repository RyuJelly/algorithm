from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(N)]
sum_list = []
# 가로
for i in range(N):
    for j in range(M-1):
        # 기준 2블럭
        s = arr[i][j] + arr[i][j+1]
        try:
            sum_list.append(s + arr[i-1][j-1] + arr[i-1][j])
        except:
            pass
        try:
            sum_list.append(s + arr[i-1][j] + arr[i-1][j+1])
        except:
            pass
        try:
            sum_list.append(s + arr[i-1][j+1] + arr[i-1][j+2])
        except:
            pass
        try:
            sum_list.append(s + arr[i][j+2] + arr[i-1][j])
        except:
            pass
        try:
            sum_list.append(s + arr[i][j+2] + arr[i-1][j+1])
        except:
            pass
        try:
            sum_list.append(s + arr[i][j+2] + arr[i-1][j+2])
        except:
            pass
        try:
            sum_list.append(s + arr[i][j+2] + arr[i+1][j+2])
        except:
            pass
        try:
            sum_list.append(s + arr[i][j+2] + arr[i+1][j+1])
        except:
            pass
        try:
            sum_list.append(s + arr[i][j+2] + arr[i+1][j])
        except:
            pass
        try:
            sum_list.append(s + arr[i][j+2] + arr[i][j-1])
        except:
            pass
# 세로
for i in range(N-1):
    for j in range(M):
        # 기준 2블럭
        s = arr[i][j] + arr[i+1][j]
        try:
            sum_list.append(s + arr[i-1][j+1] + arr[i][j+1])
        except:
            pass
        try:
            sum_list.append(s + arr[i+1][j+1] + arr[i+2][j+1])
        except:
            pass
        try:
            sum_list.append(s + arr[i+2][j] + arr[i][j+1])
        except:
            pass
        try:
            sum_list.append(s + arr[i+2][j] + arr[i+1][j+1])
        except:
            pass
        try:
            sum_list.append(s + arr[i+2][j] + arr[i+2][j+1])
        except:
            pass
        try:
            sum_list.append(s + arr[i+2][j] + arr[i+2][j-1])
        except:
            pass
        try:
            sum_list.append(s + arr[i+2][j] + arr[i+1][j-1])
        except:
            pass
        try:
            sum_list.append(s + arr[i+2][j] + arr[i][j-1])
        except:
            pass
        try:
            sum_list.append(s + arr[i+2][j] + arr[i-1][j])
        except:
            pass
print(max(sum_list))