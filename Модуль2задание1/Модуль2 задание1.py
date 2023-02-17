import json
import hashlib
import rsa

with open('Task1-block.json') as file:
    file = json.load(file)
    fe = str(file)
fe = fe.replace(" ","").replace("'",'"')

s = open('key.txt', 'r')
f = s.readlines()
d = int(f[0][:-1])
e = int(f[1][:-1])
n = int(f[2][:-1])
p = int(f[3][:-1])
q = int(f[4][:-1])

privkey = rsa.PrivateKey(d=d,e=e,n=n,p=p,q=q)
pubkey = rsa.PublicKey(e=e,n=n)

signature = '0c405ae18476b3bb6fca4cfbd02497064d8379f485796bb7855fcd6c4551b0fdb1704bac3f9700eed849dbf500c86dc33ac600099000991f2893bf2fd84206c3'

s = rsa.sign(fe.encode(), privkey, 'SHA-1')
print(s.hex())

#v = rsa.verify(fe.encode(), signature, pubkey)
#print(v)






