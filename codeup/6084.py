h,b,c,s = map(int,input().split())

#mb = (h*b*c*s)/800000
mb = h*b*c*s/8/1024/1024

print(f'{round(mb,1)} MB')