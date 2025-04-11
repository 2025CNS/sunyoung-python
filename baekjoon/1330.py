a,b = map(int,input().split())
re = 0

if a > b:
    re='>'
elif a < b:
    re='<'
else:
    re='=='

print(re)