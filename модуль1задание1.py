import json
import hashlib
with open('Task1_tx.json') as file:
    file = json.load(file)
    f = str(file)

f = f.replace(" ","").replace("'",'"')

a = hashlib.sha256(f.encode()).hexdigest()

b = file['value'] ** 2
print(b)
