n = int(input())

for _ in range(n):
    a = list(map(str,input().split()))
    for i in range(len(a[1])):
        print(a[1][0+i:1+i]*int(a[0]),end='')
        
    print('')