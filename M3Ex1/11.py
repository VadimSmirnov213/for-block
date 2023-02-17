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

import hashlib
for i in range(0,24):
    if ch[i]['hash'] != ch[i + 1]['pre_hash']:
        print(ch[i]['hash'])

def check_hash(block, block_id):
    n_block = block.copy()
    del n_block["hash"]
    if block_id != 0:
        del n_block["sign"]
    hsh = hashlib.md5(json.dumps(n_block, separators=(",", ":")).encode()).hexdigest()
    if block["hash"] != hsh:
        block["hash"] = hsh
        print(block_id, "hash", block["hash"])
    return block
for block_id, block in enumerate(ch):
    ch[block_id] = check_hash(block, block_id)
    
