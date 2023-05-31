n=int(input())
a=0
b=1
c=a+b
print(a,b,c,end=' ')
for i in range(3,n):
    a=b
    b=c
    c=a+b
    print(c,end=' ')