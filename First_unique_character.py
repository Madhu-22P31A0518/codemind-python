a=input()
d=a.lower()
e=[]
for i in d:
    if d.count(i)==1:
        e.append(i)
if len(e)==0:
    print("-1")
else:
    print(e[0])