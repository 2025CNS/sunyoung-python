user = list(map(str,input()))
re = []

for i in user:
    if ord(i) < ord('a'):
        re.append(chr(ord(i)+32))
    else:
        re.append(chr(ord(i)-32))


for j in re:
    print(j,end='')
#print(ord("A"),ord('a'))