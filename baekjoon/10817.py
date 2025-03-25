a, b, c = map(int,input().split())
# 50 60 70

if a >= b: 
    m = b # m이 더 작은  
    x = a
else: # m = 50 / x = 60
    m = a
    x = b

if x <= c: # 60 <= 70 / re = 60 
    re = x

elif m >= c: # 50 >= 70
    re = m
elif m <= c: # 
    re = c

print(re)