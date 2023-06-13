n=int(input())
a=list(map(int,input().split()))
q=[]
for i in a:
    d=str(i)
    e=len(d)
    q.append(e)
# print(q)
f=max(q)
# print(f)
for j in q:
    x=q.count(f)
print(x)