w = 'Blockchain'
import hashlib
a = hashlib.sha3_384(w.encode()).hexdigest()
f = a + 'Buterin'
c = 0
A=[]
for i in range(100000, 1000000):
    h2 = f + str(i)



    a = hashlib.sha384(h2.encode()).hexdigest()
    if a[0:4] == 'cafe':
        A.append(i)

        c=c+1
    a = hashlib.sha224(h2.encode()).hexdigest()
    if a[0:4] == 'cafe':


        A.append(i)
        print(i)
        c = c + 1
    
    a = hashlib.sha256(h2.encode()).hexdigest()
    if a[0:4] == 'cafe':


        A.append(i)
        c = c + 1
    a = hashlib.sha512(h2.encode()).hexdigest()
    if a[0:4] == 'cafe':


        A.append(i)
        c = c + 1
    
