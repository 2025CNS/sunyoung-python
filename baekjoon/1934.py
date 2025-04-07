'''n = int(input())
re= 0


for _ in range(n):
    a, b = map(int, input().split())
    
    if a == 1 or b == 1:
        re = a*b
        
    else:
        for _ in range(2,a*b+1):
            if _%a==0 and _%b==0:
                re = _
                
                break

    print(re)'''

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    
    x, y = a, b
    while y:
        x, y = y, x % y  # 유클리드 알고리즘

    lcm = a * b // x
    print(lcm)



