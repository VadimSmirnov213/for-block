import hashlib, os, json, rsa
from pathlib import Path

direct = sorted(os.listdir(os.path.dirname(__file__)))[:-1]
BASE_DIR = Path(__file__).resolve().parent.parent
chain = []


for i in range(24):
    with open(f"{os.path.dirname(__file__)}/block{i}.txt") as file:
        chain.append(json.load(file))


def check_index(block, block_id):
    if block["index"] != block_id:
        block["index"] = block_id
        print(f"{block_id} index of {block['index']}")
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


def check_prehash(block, block_id):
    if block_id == 0:
        if block["pre_hash"] != "0x0":
            block["pre_hash"] = "0x0"
            print(block_id, "pre_hash", block["pre_hash"])
    else:
        if block["pre_hash"] != chain[block_id-1]["hash"]:
            block["pre_hash"] = chain[block_id-1]["hash"]
            print(block_id, "pre_hash", block["pre_hash"])
    return block


def mercule(transactions: list):
    lst = []
    while len(transactions) > 1:
        for i in range(0, len(transactions), 2):
            if i + 1 == len(transactions):
                toHash = transactions[i]*2
            else:
                toHash = transactions[i] + transactions[i+1]

            lst.append(hashlib.md5(str(toHash).encode()).hexdigest())
        transactions = lst
        lst = []
    return transactions[0]


def check_datahash(block, block_id):
    if block_id == 0:
        return block
    transactions = block["data"]
    topHash = mercule(transactions)
    if block["datahash"] != topHash:
        block["datahash"] = topHash
        print(block_id, "datahash", block["datahash"])
    return block


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



def check_sign(block, block_id):
    if block_id == 0:
        return block
    b_sign = block["sign"]
    del block["sign"]
    str_block = json.dumps(block, separators=(",", ":"))
    creator = block["creator"]
    with open(f"{BASE_DIR}\Keys\{creator}.key") as key:
        key = key.read().split("\n")
    keys = {}
    for i in key:
        keys[i[0]] = int(i[3:])
    priv = rsa.PrivateKey(keys["n"], keys["e"], keys["d"], keys["p"], keys["q"])
    sign = rsa.sign(str_block.encode(), priv, "SHA-1").hex()
    if sign != b_sign:
        block["sign"] = sign
        print(block_id, "sign", block["sign"])

    return block

# enumerate возвращает список эллементов, где нулевой - id, первый - эллемент
for block_id, block in enumerate(chain):
    chain[block_id] = check_index(block, block_id)
    chain[block_id] = check_datahash(block, block_id)
    chain[block_id] = check_prehash(block, block_id)
    chain[block_id] = check_nonce(block, block_id)
    chain[block_id] = check_hash(block, block_id)
    #chain[block_id] = check_sign(block, block_id)

