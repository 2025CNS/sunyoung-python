n = int(input())
a = list()
#max_key={}

for _ in range(n):
    n2 = int(input())
    for i in range(n2):
        s , col = input().split()
        a.append([int(col),s])
        a.sort(reverse=True)

    print(a[0][1])





