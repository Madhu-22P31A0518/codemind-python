n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s=s+i
d=s//len(a)
if d in a:
    print(True)
else:
    print(False)