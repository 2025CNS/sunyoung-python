a = [1,1,2,2,2,8]

user = list(map(int,input().split()))

re = list()

for i in range(6):
    re.append(a[i]-user[i])

for _ in range(6):
    print(re[_],end=' ')