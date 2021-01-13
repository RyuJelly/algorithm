def solution(s):
    count = 0
    slist = list(s)
    for i in range(len(slist)):
        if slist[i] == ' ':
            count = 0
        else:
            if count%2:
                slist[i] = slist[i].lower()
            else:
                slist[i] = slist[i].upper()
            count += 1
    answer = ''.join(slist)
    return answer