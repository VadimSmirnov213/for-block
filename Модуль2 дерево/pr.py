import hashlib
A = []
tr = open('45.txt')
for line in tr:
    line = line.rstrip('\n')
    A.append(line)
def top(u):
    t = []
    if len(u) == 1:
        print(hashlib.sha256(u[0].encode()).hexdigest())
    if len(u) > 1:
        x = 0
        while x < len(u):
            t.append(u[x] + u[x + 1])
            x = x + 2
        u.clear()
        for i in range(0, len(u)):
            u[i] = hashlib.sha256(u[i].encode()).hexdigest()
        
        for i in range(0, len(t)):
            u.append(t[i])
        top(u)
top(A)
