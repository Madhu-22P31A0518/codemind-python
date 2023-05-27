p,r,t=map(int,input().split())
a=(1+(r/100))
d=pow(a,t)
f=p*d
e=f-p
print('%.2f' %f)