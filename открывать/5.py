import hashlib

sl='Blockchain'

#b = hashlib.sha3_384(sl.encode()).hexdigest()
sl='835ab9759f5bbfe90d006333dda669dfd7bea13711804b0a44416f46f6b7c0c6c5be95727e5885539526e2729dec6639Buterin'
c=0
#print(sl[0:4])

A=[]
for i in range(100000, 1000000):
    h2 = sl + str(i)



    a = hashlib.sha384(h2.encode()).hexdigest()
    if a[0:4] == 'cafe':
        A.append(i)

        c=c+1
    a = hashlib.sha224(h2.encode()).hexdigest()
    if a[0:4] == 'cafe':


        A.append(i)
        c = c + 1
    a = hashlib.sha1(h2.encode()).hexdigest()
    if a[0:4] == 'cafe':


        A.append(i)
        c = c + 1
    a = hashlib.sha256(h2.encode()).hexdigest()
    if a[0:4] == 'cafe':


        A.append(i)
        c = c + 1
    a = hashlib.sha3_256(h2.encode()).hexdigest()
    if a[0:4] == 'cafe':


        A.append(i)
        c = c + 1
    a = hashlib.sha3_224(h2.encode()).hexdigest()
    if a[0:4] == 'cafe':


        A.append(i)

        c = c + 1
    a = hashlib.sha3_384(h2.encode()).hexdigest()
    if a[0:4] == 'cafe':

        A.append(i)

        c = c + 1
    a = hashlib.sha384(h2.encode()).hexdigest()
    if a[0:4] == 'cafe':


        A.append(i)
        c = c + 1
    a = hashlib.sha3_512(h2.encode()).hexdigest()
    if a[0:4] == 'cafe':


        A.append(i)
        c = c + 1

print(hashlib.sha3_384(sl.encode()).hexdigest())
print("sha3_384")
print('cafe80519f66883c66b90a87bba7ee0aad3b3a39cdfbb41ce091ba9110834ccc247158f35d1a9d1d07b4991ce5ec5f7c')

print(min(A))

print(c)



