n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
c=0
for i in a:
    if i in b:
        c+=1
if c==0 or c<n:
    print(False)
elif c==n:
    print(True)