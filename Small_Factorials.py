def fact(n):
    if n==0:
        print('0')
    else:
        p=1
        for i in range(1,n+1):
            p=p*i
        print(p)
a=int(input())
for j in range(1,a+1):
    n=int(input())
    fact(n)