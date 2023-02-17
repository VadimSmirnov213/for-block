import hashlib
import json

ch = []
with open('block0.txt') as file:
    ch.append(json.load(file))
with open('block1.txt') as file:
    ch.append(json.load(file))
with open('block2.txt') as file:
    ch.append(json.load(file))
with open('block3.txt') as file:
    ch.append(json.load(file))
with open('block4.txt') as file:
    ch.append(json.load(file))
with open('block5.txt') as file:
    ch.append(json.load(file))
with open('block6.txt') as file:
    ch.append(json.load(file))
with open('block7.txt') as file:
    ch.append(json.load(file))
with open('block8.txt') as file:
    ch.append(json.load(file))
with open('block9.txt') as file:
    ch.append(json.load(file))
with open('block10.txt') as file:
    ch.append(json.load(file))
with open('block11.txt') as file:
    ch.append(json.load(file))
with open('block12.txt') as file:
    ch.append(json.load(file))
with open('block13.txt') as file:
    ch.append(json.load(file))
with open('block14.txt') as file:
    ch.append(json.load(file))
with open('block15.txt') as file:
    ch.append(json.load(file))
with open('block16.txt') as file:
    ch.append(json.load(file))
with open('block17.txt') as file:
    ch.append(json.load(file))
with open('block18.txt') as file:
    ch.append(json.load(file))
with open('block19.txt') as file:
    ch.append(json.load(file))
with open('block20.txt') as file:
    ch.append(json.load(file))
with open('block21.txt') as file:
    ch.append(json.load(file))
with open('block22.txt') as file:
    ch.append(json.load(file))
with open('block23.txt') as file:
    ch.append(json.load(file))
with open('block24.txt') as file:
    ch.append(json.load(file))

a=[]

w = len(a)
s = 1
def mercule(u):
    global w
    global s
    t=[]
    if len(u)==1:
        return hashlib.sha256(u[0].encode()).hexdigest()
    if len(u)>1:
        if len(u)%2>0:
            u.append(u[len(u)-1])
            w = w + 1
        for i in range(0,len(u)):
            u[i]=hashlib.sha256(u[i].encode()).hexdigest()
        x=0
        while x<len(u):
            t.append(u[x]+u[x+1])
            x=x+2
        u.clear()
        s = s + 1
        for i in range(0,len(t)):
            u.append(t[i])
            
def check_datahash(block, block_id):
    if block_id == 0:
        return block
    transactions = block["data"]
    topHash = mercule(transactions)
    if block["datahash"] != topHash:
        block["datahash"] = topHash
        print(block_id, "datahash", block["datahash"])
    return block

for block_id, block in enumerate(ch):
    
    ch[block_id] = check_datahash(block, block_id)
