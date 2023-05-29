n=int(input())
a=list(map(int,input().split()))
e=[]
for i in a:
    if a.count(i)>=n/2:
        e.append(i)
d=set(e)
for j in d:
    print(j)