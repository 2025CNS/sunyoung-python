n, x = map(int,input().split())
a = []


y = list(map(int,input().split()))

for _ in range(n): #0, 1, 2..
    if x > y[_]: # y가 x보다 작으면
        a.append(y[_]) #a 안에


for i in range(len(a)):
    print(a[i],end=' ')