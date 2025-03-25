n = int(input())
re = 0
list_ = []

for i in range(n):   
    a, b, c = map(int,input().split())
    if a == b and b == c:
        re = 10000 + (a * 1000)
    elif a == b or b == c or a ==c:
        if a == b:
            re = 1000 + (a * 100)
        elif b == c: 
            re = 1000 + (b * 100)
        else:
            re = 1000 + (c * 100)
    else:
        re = max(a,b,c) * 100
    list_.append(re)

print(max(list_))
