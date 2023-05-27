n=int(input())
c=0
for i in range(1,n):
    if n%i==0:
        if i*i==n:
            c+=1
if c==0:
    print(False)
else:
    print(True)