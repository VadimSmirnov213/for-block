import hashlib
a=[]
f=open('45.txt')
for line in f:
    line=line.rstrip('\n')
    a.append(line)
def tophash(u):
    t=0
    if len(u)==1:
        print(hashlib.sha256(str(u[0]).encode()).hexdigest())
        if len(u)%2>1:
            list(u).append(u[len(u)-1])
        for i in range(0,len(u)):
            u[i]=hashlib.sha256(str(u[i]).encode()).hexdigest()
        x=0
        while x<len(u):
            list(t).append(u[x]+u[x+1])
            x=x+2
        list(u).clear()
        for i in range(0,len(t)):
            list(u[i]).append(list(t[i]))

    tophash(list(u))
tophash(a)


