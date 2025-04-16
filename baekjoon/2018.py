'''user = int(input())
a = user
count = 0
re = 0

while True:
    if a == 0:
        break
    for i in range(a,0,-1):
        re += i
        if re == user:
            count += 1
        elif re > user:
            break
    a -=1
    re = 0

print(count)'''

N = int(input())
count = 0
k = 1

while k * (k + 1) // 2 <= N:
    if (N - (k * (k - 1) // 2)) % k == 0:
        count += 1
    k += 1

print(count)
