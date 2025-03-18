a,m,d,n = map(int,input().split())

#re = (a*-2-1)**(n-5)

for i in range(1,n):
    a = a*m+d

print(a)