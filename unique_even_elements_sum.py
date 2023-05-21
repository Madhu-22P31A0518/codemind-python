n=int(input())
a=list(map(int,input().split()))
s=0
d=set(a)
for i in d:
    if i%2==0:
        s=s+i
print(s)