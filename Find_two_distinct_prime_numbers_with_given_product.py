n=int(input())
c=0
for i in range(2,n):
    if n%i==0:
        c+=1
        print(i,end=' ')
if c==0:
    print('-1')
