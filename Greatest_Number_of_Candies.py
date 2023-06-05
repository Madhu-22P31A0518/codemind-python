n=int(input())
a=list(map(int,input().split()))
k=int(input())
d=max(a)
for i in a:
    if i+k>=d:
        print(True,end=' ')
    else:
        print(False,end=' ')