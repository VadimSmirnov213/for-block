import hashlib
a=[]
tree_file=open("455.txt")
for line in tree_file:
    line = line.rstrip('\n')
    a.append(line)
w = len(a)
s = 1
def tophash(u):
    global w
    global s
    t=[]
    if len(u)==1:
        print(hashlib.md5(u[0].encode()).hexdigest())
    if len(u)>1:
        if len(u)%2>0:
            u.append(u[len(u)-1])
            w = w + 1
        for i in range(0,len(u)):
            u[i]=hashlib.md5(u[i].encode()).hexdigest()
        x=0
        while x<len(u):
            t.append(u[x]+u[x+1])
            x=x+2
        u.clear()
        s = s + 1
        for i in range(0,len(t)):
            u.append(t[i])
        tophash(u)
tophash(a)
print('lists', w)

