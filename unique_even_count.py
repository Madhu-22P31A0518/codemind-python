n=int(input())
a=list(map(int,input().split()))
d=set(a)
c=0
for i in d:
    if i%2==0:
        c+=1
print(c)