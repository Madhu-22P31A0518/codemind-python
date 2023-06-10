n=int(input())
for i in range(1,n+1):
    a=int(input())
    b=list(map(int,input().split()))
    s=0
    d=a*(a+1)//2
    for i in b:
        s=s+i
    print(d-s)