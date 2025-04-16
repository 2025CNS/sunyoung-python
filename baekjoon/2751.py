'''n = int(input())
li = []

for i in range(n):
    user = int(input())
    li.append(user)

li = set(li)
li = list(li)

li.sort()

for j in li:
    print(j)'''

import sys

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    user = int(sys.stdin.readline())
    li.append(user)

li = sorted(set(li))

for j in li:
    print(j)
