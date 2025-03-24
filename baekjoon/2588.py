a = int(input())
b = list(input()) # '3','7','5'

print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))

re = a*int(b[2]) + (a*int(b[1])*10) + (a*int(b[0])*100)
print(re)