import hashlib
import json
import rsa
ch = []
for i in range(25):
    a = 'block' + str(i) + '.txt'
    with open(a) as file:
        ch.append(json.loads(file.read()))
        #a = ''
    


print(9, 'index', 9)


        

def cgu(block, block_id):
    b_n = block.copy()
    del b_n['hash']
    if block_id != 0:
        del b_n['sign']
    hsh = hashlib.sha3_256(json.dumps(b_n, separators=(",",":")).encode()).hexdigest()
    if hsh != block['hash']:
        block['hash'] = hsh
        print(block['index'], 'hash', block['hash'])
    return block


def check_prehash(block, block_id):
    if block_id == 0:
        if block["pre_hash"] != "0x0":
            block["pre_hash"] = "0x0"
            print(block_id, "pre_hash", block["pre_hash"])
    else:
        if block["pre_hash"] != ch[block_id-1]["hash"]:
            block["pre_hash"] = ch[block_id-1]["hash"]
            print(block_id, "pre_hash", block["pre_hash"])
    return block
for block_id, block in enumerate(ch):
    ch[block_id] = cgu(block, block_id)
    ch[block_id] = check_prehash(block, block_id)

for i in range(0,25):
    if len(ch[i]['data']) == 4:
        a = ch[i]['data'][0]
        b = ch[i]['data'][1]
        c = ch[i]['data'][2]
        d = ch[i]['data'][3]
        s1 = a + b
        s2 = c + d
        s1 = hashlib.sha3_256(s1.encode()).hexdigest()
        s2 = hashlib.sha3_256(s2.encode()).hexdigest()
        s = s1 + s2
        s = hashlib.sha3_256(s.encode()).hexdigest()
        if s != ch[i]['datahash']:
            print(i,'datahash', s)
    elif len(ch[i]['data']) == 2:
        a = ch[i]['data'][0]
        b = ch[i]['data'][1]
        s1 = a + b
        s1 = hashlib.sha3_256(s1.encode()).hexdigest()
        if s1 != ch[i]['datahash']:
            print(i,'datahash', s1)
    elif len(ch[i]['data']) == 1:
        if ch[i]['data'][0] != ch[i]['datahash']:
            print(i,'datahash', ch[i]['data'][0])
    elif len(ch[i]['data']) == 6:
        a = ch[i]['data'][0]
        b = ch[i]['data'][1]
        c = ch[i]['data'][2]
        d = ch[i]['data'][3]
        e = ch[i]['data'][4]
        f = ch[i]['data'][5]
        s1 = a + b
        s2 = c + d
        s3 = e + f
        s1 = hashlib.sha3_256(s1.encode()).hexdigest()
        s2 = hashlib.sha3_256(s2.encode()).hexdigest()
        s3 = hashlib.sha3_256(s3.encode()).hexdigest()
        s1 = s1 + s2
        s2 = s3 + s3
        s1 = hashlib.sha3_256(s1.encode()).hexdigest()
        s2 = hashlib.sha3_256(s2.encode()).hexdigest()
        s = s1 + s2
        s = hashlib.sha3_256(s.encode()).hexdigest()
        if s != ch[i]['datahash']:
            print(i,'datahash', s)


for i in range(1,25):        
    d = ch[i]['creator']
    f = d + '.key'
    tr = open(f)
    A = []
    for line in tr:
        line = line.rstrip('\n')
        A.append(line.replace('d: ','').replace('e: ','').replace('n: ','').replace('p: ','').replace('q: ',''))

    pubkey = rsa.PublicKey(e=int(A[1]),n=int(A[2]))
    privkey = rsa.PrivateKey(d=int(A[0]),e=int(A[1]),n=int(A[2]),p=int(A[3]),q=int(A[4]))
    sg = ch[i]['sign']
    del ch[i]['sign']
    d = str(ch[i])
    d = d.replace("'",'"').replace(" ",'')

    s = rsa.sign(d.encode(), privkey, 'SHA-224')
    s = s.hex()
    if s != sg:
        print(i, 'sign', s)
        A.clear()
    else:
        A.clear()
        
      






    
       
