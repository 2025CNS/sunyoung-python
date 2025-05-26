re = 0

li = list(map(int,input().split()))
for i in li:
    #print(i*i)
    re += i*i

print(re%10)