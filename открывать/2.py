import json
import hashlib

with open('Task2_block.json') as file:
    file = json.loads(file.read())
    #file=str(file).replace("'",'"').replace(", ",',').replace(": ",':')



hash='111112'


while hash[-4:]!='abcd':
    res=hashlib.sha3_384(str(file).replace("'",'"').replace(", ",',').replace(": ",':').encode()).hexdigest()
    hash=res
    file['nonce']+=1
print(file['nonce'])
