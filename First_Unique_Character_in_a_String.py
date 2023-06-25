n=input()
e=[]
c=0
for i in n:
    if n.count(i)==1:
        d=n.index(i)
        e.append(d)
        c+=1
if c==0:
    print('-1')
else:
    print(e[0])