'''import hashlib
a='DistributedRegistry2020'

f=hashlib.sha256(a.encode()).hexdigest()
b=''



for i in range(1000,10001):
    c=f+str(i)

    d=hashlib.sha3_384(c.encode()).hexdigest()
    if d==b:
        print(i)
'''
print('p')