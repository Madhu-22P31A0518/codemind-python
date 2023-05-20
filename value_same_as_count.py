n=int(input())
a=list(map(int,input().split()))
c=0
e=[]
for i in a:
    if a.count(i)==i:
        e.append(i)
d=set(e)
f=len(d)
print(f)