# 2480 주사위 세개
A, B, C = map(int,input().split())
list = []
list.append(int(A))
list.append(int(B))
list.append(int(C))
list.sort()

list_s = set(list)

if len(list_s) == 1:
    print(10000 + list[0] * 1000)
elif len(list_s) == 3:
    print(list[-1]*100)
else:
    print(1000 + list[1] * 100)