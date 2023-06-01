n=int(input())
if n==0:
    print('0')
elif n<=4:
    print('1')
elif n%4!=0:
    d=n//4
    print(d+1)
else:
    d=n//4
    print(d)