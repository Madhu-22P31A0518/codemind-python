n=int(input())
for i in range(1,n+1):
    a=input()
    e=[]
    d=a[::-1]
    e.append(d)
    if a==d:
        print("YES",end=' ')
        if len(a)%2==0:
            print('EVEN')
        else:
            print("ODD")
    else:
        print("NO")