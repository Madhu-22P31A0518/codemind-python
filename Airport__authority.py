n=int(input())
e=[]
c=0
for i in range(1,n+1):
    a=int(input())
    e.append(a)
b=int(input())
for j in e:
    if j<=b:
        c+=1
    else:
        c+=2
print(c)