import math
a,b,c=map(int,input().split())
e=a+b+c
s=e/2
d=s*(s-a)*(s-b)*(s-c)
k=math.sqrt(d)
print('%.2f' %k)