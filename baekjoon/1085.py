x, y, w, h = map(int,input().split())
re1 = 0
re2 = 0
re = 0

if w-x < x:
    re1 = w-x
else:
    re1 = x
if h-y < y:
    re2 = h-y
else:
    re2 = y

if re1 < re2:
    re = re1
else:
    re = re2

print(re)