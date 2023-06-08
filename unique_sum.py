n=int(input())
a=list(map(int,input().split()))
c=0
d=set(a)
for i in d:
    c=c+i
print(c)