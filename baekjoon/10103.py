n = int(input())
re1 = 100
re2 = 100

for _ in range(n):
    h1, h2 = map(int,input().split())
    
    if h1 > h2:
        re2 -= h1
    elif h1 < h2:
        re1 -= h2

print(re1)
print(re2)
    
