n = int(input())
no = 0
yes = 0
re = 0

for _ in range(n):
    cc = input()

    if cc == '0':
        no +=1
    else:
        yes += 1

if yes > no:
    re = 'Junhee is cute!'
else:
    re = 'Junhee is not cute!'

print(re)