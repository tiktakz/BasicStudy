# 2480 주사위 세개
# 같은 숫자 3개 >> 10000 + (나온 숫자 * 1000)
# 같은 숫자 2개 >> 1000 + (나온 숫자 * 100)
# 같은 숫자 없으면 >> 가장큰 숫자 * 100

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