import json
import hashlib
with open('Task2_block.json') as file:
    file = json.loads(file.read())
while True:
    a = str(file).replace(' ','').replace("'",'"')
    b = hashlib.sha3_224(a.encode()).hexdigest()
    if b[-4:] == 'abcd':
        print(file['nonce'])
        break
    else:
        file['nonce'] += 1
         
    
