n=int(input())
a=list(map(int,input().split()))
q=[]
for i in a:
    d=str(i)
    e=len(d)
    q.append(e)
for j in q:
    s=min(q)
    g=q.count(s)
print(g)