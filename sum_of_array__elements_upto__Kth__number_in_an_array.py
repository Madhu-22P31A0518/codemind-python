n=int(input())
a=list(map(int,input().split()))
b=int(input())
s=0
for i in a:
    s=s+i
    if i==b:
        break
print(s)