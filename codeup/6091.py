h1,h2,h3= map(int,input().split())

d = 1
while d%h1!=0 or d%h2!=0 or d%h3!=0 :
  d += 1

print(d)