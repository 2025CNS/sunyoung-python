s = int(input())
re = 0
for i in range(1,s+1):

    re += i

    if re > s:
        print(i-1)
        break
    if re >= s:
        print(i)
        break

    