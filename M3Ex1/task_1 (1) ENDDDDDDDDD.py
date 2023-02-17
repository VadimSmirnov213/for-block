import hashlib, json, rsa
chain = []

for i in range(25):
    a = 'block' + str(i) + '.txt'
    with open(a) as file:
        chain.append(json.loads(file.read()))

#chain[9]['index'] = 9
#print(9, 'index', 9)
def check_index(block, block_id):
    if block["index"] != block_id:
        block["index"] = block_id
        print(f"{block_id} index of {block['index']}")
    return block

def check_prehash(block, block_id):
    if block_id != 0:
        if block["pre_hash"] != chain[block_id-1]["hash"]:
            block["pre_hash"] = chain[block_id-1]["hash"]
            print(block_id, "pre_hash", block["pre_hash"])
    return block
'''
for i in range(25):
    if len(chain[i]['data']) == 4:
        a = chain[i]['data'][0]
        b = chain[i]['data'][1]
        c = chain[i]['data'][2]
        d = chain[i]['data'][3]
        s1 = a + b
        s2 = c + d
        s1 = hashlib.md5(s1.encode()).hexdigest()
        s2 = hashlib.md5(s2.encode()).hexdigest()
        s = s1 + s2
        s = hashlib.md5(s.encode()).hexdigest()
        if s != chain[i]['datahash']:
            chain[i]['datahash'] = s
            print(i,'datahash', s)
    elif len(chain[i]['data']) == 2:
        a = chain[i]['data'][0]
        b = chain[i]['data'][1]
        s1 = a + b
        s1 = hashlib.md5(s1.encode()).hexdigest()
        if s1 != chain[i]['datahash']:
            chain[i]['datahash'] = s1
            print(i,'datahash', s1)
    elif len(chain[i]['data']) == 1:
        if chain[i]['data'][0] != chain[i]['datahash']:
            print(i,'datahash', chain[i]['data'][0])
    elif len(chain[i]['data']) == 6:
        a = chain[i]['data'][0]
        b = chain[i]['data'][1]
        c = chain[i]['data'][2]
        d = chain[i]['data'][3]
        e = chain[i]['data'][4]
        f = chain[i]['data'][5]
        s1 = a + b
        s2 = c + d
        s3 = e + f
        s1 = hashlib.md5(s1.encode()).hexdigest()
        s2 = hashlib.md5(s2.encode()).hexdigest()
        s3 = hashlib.md5(s3.encode()).hexdigest()
        s1 = s1 + s2
        s2 = s3 + s3
        s1 = hashlib.md5(s1.encode()).hexdigest()
        s2 = hashlib.md5(s2.encode()).hexdigest()
        s = s1 + s2
        s = hashlib.md5(s.encode()).hexdigest()
        if s != chain[i]['datahash']:
            chain[i]['datahash'] = s1
            print(i,'datahash', s)
 '''
t = []
for i in range(1, 25):
    x = 0
    while x < len(chain[i]['data']):
        t.append(chain[i]['data'][x] + chain[i]['data'][x + 1])
        x += 2
    
                 


def find_nonce(block):
    nonce = 0
    while True:
        block["nonce"] = nonce
        hsh = hashlib.md5(json.dumps(block, separators=(",", ":")).encode()).hexdigest()
        if hsh[:3] == "000":
            block["hash"] = hsh
            break
        nonce += 1
    return block["nonce"]


def check_nonce(block, block_id):
    n_block = block.copy()
    del n_block["hash"]
    if block_id != 0:
        del n_block["sign"]
    nonce = find_nonce(n_block)
    if block["nonce"] != nonce:
        block["nonce"] = nonce
        print(block_id, "nonce", block["nonce"])

    return block


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




# enumerate возвращает список эллементов, где нулевой - id, первый - эллемент
for block_id, block in enumerate(chain):
    chain[block_id] = check_index(block, block_id)
    chain[block_id] = check_prehash(block, block_id)
    chain[block_id] = check_nonce(block, block_id)
    chain[block_id] = check_hash(block, block_id)
    


for i in range(1,25):        
    d = chain[i]['creator']
    f = d + '.key'
    tr = open(f)
    A = []
    for line in tr:
        line = line.rstrip('\n')
        A.append(line.replace('d: ','').replace('e: ','').replace('n: ','').replace('p: ','').replace('q: ',''))

    pubkey = rsa.PublicKey(e=int(A[1]),n=int(A[2]))
    privkey = rsa.PrivateKey(d=int(A[0]),e=int(A[1]),n=int(A[2]),p=int(A[3]),q=int(A[4]))
    sg = chain[i]['sign']
    del chain[i]['sign']
    d = str(chain[i])
    d = d.replace("'",'"').replace(" ",'')

    s = rsa.sign(d.encode(), privkey, 'SHA-1')
    s = s.hex()
    if s != sg:
        print(i, 'sign', s)
        A.clear()
    else:
        A.clear()

