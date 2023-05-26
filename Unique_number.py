n=input()
a=list(n)
b=set(a)
c=list(b)
if sorted(a)==sorted(c):
    print('Unique Number')
else:
    print('Not Unique Number')