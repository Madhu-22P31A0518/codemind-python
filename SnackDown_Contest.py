n=int(input())
for i in range(1,n+1):
    a=int(input())
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    d=b+c
    e=set(d)
    s=0
    f=a*(a+1)//2
    for j in e:
        s=s+j
    if s==f:
        print('YES')
    else:
        print("NO")