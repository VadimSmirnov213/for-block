import hashlib
import json
with open('Task1_sample_tx.json') as file:
    file = json.loads(file.read())
    file = str(file)
file = file.replace(' ','').replace("'",'"')
print(hashlib.sha256(file.encode()).hexdigest())
