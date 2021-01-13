def solution(a, b):
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    dlist = [31,29,31,30,31,30,31,31,30,31,30,31]
    x = 0
    for i in range(a-1):
        x += dlist[i]
    x += b
    answer = day[x%7-1]
    return answer