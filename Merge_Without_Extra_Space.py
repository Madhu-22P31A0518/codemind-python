n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    d=list(map(int,input().split()))
    f=c+d
    e=sorted(f)
    print(*e)