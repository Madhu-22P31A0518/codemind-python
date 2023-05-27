n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        if i*(i+1)==n:
            c+=1
if c==0:
    print('NO')
else:
    print('YES')