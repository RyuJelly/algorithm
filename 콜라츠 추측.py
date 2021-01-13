def solution(num):
    count = 0
    if num == 1:
        return count
    for i in range(500):
        count = i + 1
        if num%2:
            num = num * 3 + 1
        else:
            num = num/2
        if num == 1:
            break
    if num != 1:
        count = -1
    return count