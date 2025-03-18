n = int(input())
a = list(map(int,input().split()))

for i in range(n-1,-1,-1):   #번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
    print(a[i],end=' ')