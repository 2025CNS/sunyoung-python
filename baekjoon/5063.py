n = int(input())

for _ in range(n):
    a,b,c = map(int,input().split())
    if a+c < b:
        re = 'advertise'
    elif a+c == b:
        re = 'does not matter'
    else:
        re = 'do not advertise'

    print(re)
