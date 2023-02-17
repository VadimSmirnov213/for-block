import hashlib
a = '28ea4cde0cff6b66a7980653335c38de9ec0173444f7eb26c869928cbbc89e0f5bb39e5f5e4a488ea1d401c66190d951c6324edbc6f60871812ec5fa89b47bb2'

w = 'JuniorSkills2021Final'

b1 = hashlib.sha256(w.encode()).hexdigest()
s = 0
for i in range(100000,1000000):
    b = b1 + str(i)
    c = hashlib.sha3_224(b.encode()).hexdigest()
    if c[0:2] == '01' and c[-2:] == '10':
        s = s + 1
        print('sha3_224')
        print(i)
        
    c = hashlib.sha3_384(b.encode()).hexdigest()
    if c[0:2] == '01' and c[-2:] == '10':
        s = s + 1
        print('sha3_384')
        print(i)
        
    c = hashlib.sha3_256(b.encode()).hexdigest()
    if c[0:2] == '01' and c[-2:] == '10':
        s = s + 1
        print('sha3_256')
        print(i)
        
    c = hashlib.sha3_512(b.encode()).hexdigest()
    if c[0:2] == '01' and c[-2:] == '10':
        s = s + 1
        print('sha3_512')
        print(i)
        
    
