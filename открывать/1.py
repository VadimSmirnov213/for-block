import json
import hashlib

with open("Task1_tx.json") as file:
    file = json.loads(file.read())
    file=str(file).replace("'",'"').replace(", ",',').replace(": ",':')

print(hashlib.sha256(file.encode()).hexdigest())
