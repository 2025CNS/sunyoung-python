#print(ord('a'),ord('z'))
li = []

for i in range(97, 123):
    li.append(chr(i))
#print(li)

li_ = [ 0 for q in range(26)]

user = input()
user = list(user)
#print(user)

for j in range(len(user)):
    x = li.index(user[j])
    li_[x] += 1
#print(li_)
    
for w in li_:
    print(w,end=' ')
