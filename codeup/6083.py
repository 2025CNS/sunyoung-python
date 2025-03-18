r, g, b = map(int,input().split())
t = 0
for q in range(r):

    for j in range(g):

        for i in range(b):
            
            print(q,j,i)
            t+=1

print(t)