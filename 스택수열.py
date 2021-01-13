from sys import stdin
N = int(stdin.readline())
result = [int(stdin.readline()) for _ in range(N)]
push_count = result[0]
print_s = ""
# 처음 숫자
print_s += ("+" + "\n")*push_count
print_s += "-" + "\n"
pop_count = 1    
while pop_count < N:
    if result[pop_count-1] > result[pop_count]:
        print_s += "-" + "\n"
        pop_count += 1
    elif push_count == N or (result[pop_count] < push_count):
        break
    else:
        print_s += ("+" + "\n") * (result[pop_count] - push_count)
        push_count += (result[pop_count] - push_count)
        print_s += "-" + "\n"
        pop_count += 1
if pop_count == N and push_count == N:
    print(print_s)
else:
    print("NO")