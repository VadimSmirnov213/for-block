import hashlib
import json
s = 0
with open('Task2_block.json') as file:
    file = json.loads(file.read())
while True:
    e = str(file).replace("'",'"').replace(": ",':').replace(", ",',')
    a = hashlib.sha3_224(e.encode()).hexdigest()
    if a[-4:] == 'abcd':
        print(s)
        break
    else:
        s = s + 1
        file['nonce'] +=1
    
 
