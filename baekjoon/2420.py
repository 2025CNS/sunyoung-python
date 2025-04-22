a, b = map(int,input().split())
s = a-b
re = 0
if s < 0:
    re = -s
else:
    re = s

print(re)