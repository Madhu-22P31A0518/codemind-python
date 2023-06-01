n=int(input())
a=list(map(int,input().split()))
e=[]
s=0
c=0
for i in a:
    if a.count(i)==i:
        e.append(i)
        c+=1
if c==0:
    print('-1')
else:
    d=set(e)
    for j in d:
        s=s+j
    f=s/len(d)
    print('%.2f' %f)
