k, n, m = map(int, input().split())

bb = k*n

if bb <= m:
    bb = 0
else:
    bb = bb-m
print(bb)