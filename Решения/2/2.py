import hashlib
import json
with open('Task2_block.json') as file:
    file = json.loads(file.read())
hash = 'sdfghjklkjh'
while True:
    if hash[-4:] != 'abcd':
        file['nonce'] += 1
        d = str(file).replace(' ','').replace("'",'"')
        hash = hashlib.sha3_224(d.encode()).hexdigest()
    else:
        break

    
