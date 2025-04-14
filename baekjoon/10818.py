n = int(input())

li = list(map(int,input().split()))

li.sort()

a = li[0]
b = li[len(li)-1]

print(a,b)

