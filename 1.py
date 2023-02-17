import json
import hashlib

with open("4.txt") as read_file:
    data = json.load(read_file)
    data=str(data)


    b="".join(data.split())
    c=b.replace("'", '"')
    print(hashlib.sha256(c.encode()).hexdigest())
