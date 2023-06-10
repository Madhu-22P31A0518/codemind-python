n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    for j in range(1,i+1):
        # print(j)
        if i%j==0:
            if j*j==i:
                s=s+i
print(s)