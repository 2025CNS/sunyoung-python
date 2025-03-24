n = int(input())

for i in range(n): #0,1,2,3,4
    a,b = map(int,input().split())
    print(f"Case #{i+1}: {a + b}")