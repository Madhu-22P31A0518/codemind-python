n=int(input())
s=0
z=0
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    while n!=0:
        r=n%10
        n//=10
        s=s*10+r
    for j in range(1,s+1):
        if s%j==0:
            z+=1
    if z==2:
        print('circular prime')
    else:
        print('prime but not a circular prime')
else:
    print('not prime')