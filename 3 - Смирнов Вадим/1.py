'''f=open("Task2-txlist.txt")

for line in f:
    #line=line.rstrip('\n')
    #print(line)



import json
A=[]
B=[]

with open("block0.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block1.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block2.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])
with open("block3.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block4.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block5.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block6.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block7.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block8.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block9.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block10.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block11.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block12.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block13.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block14.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block15.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block16.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block17.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block18.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block19.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block20.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block21.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block22.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block23.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])

with open("block24.txt") as file:
    file=json.loads(file.read())
    A.append(file['hash'])
    B.append(file['pre_hash'])
'''
import rsa
import hashlib
import json

with open("block5.txt") as file:
    file=json.loads(file.read())
    file=str(file).replace("'",'"').replace(', ',',').replace(': ',':')
    print(file)
d: 5471512008119507165311014388000644811377882245339034877211661620477115836526123739921630857396567937488784146067380862335843024566340810168703289106101153
e: 65537
n: 6784343628344113917188306687094849285843766317525008584766259911478738831835252426016199132986823376399046681670346779858578407356712161788361908271633901
p: 7156176244134587313811123961234873288342918517249790425134614906420297869728190073
q: 948040321659875502209818146315453244636899905389171748301063613642364437
mes=''
pub=rsa.PublicKey(e=e,n=n)
priv=rsa.PrivateKey(d=d,e=e,n=n,p=p,q=q)

sign=rsa.sign(file.encode(),priv,"SHA-1")
print(sign.hex())


