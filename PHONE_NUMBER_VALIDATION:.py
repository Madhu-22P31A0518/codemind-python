n=int(input())
d=str(n)
if len(d)!=10 or d.startswith('0'):
    print('Invalid')
else:
    print('Valid')