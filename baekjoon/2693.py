n = int(input())

for i in range(n):
    a = list(map(int,input().split()))
    a.sort(reverse=True)

    print(a[2])