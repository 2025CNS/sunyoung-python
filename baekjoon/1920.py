n = int(input())
li = set(map(int, input().split()))  # set으로 변경
a = int(input())
li1 = list(map(int, input().split()))

for i in li1:
    if i in li:
        print(1)
    else:
        print(0)


