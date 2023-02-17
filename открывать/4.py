import hashlib

sl = "JuniorSkills2021Final"

b = hashlib.sha256(sl.encode()).hexdigest()
c = 0
for i in range(100000,1000000):
    h2 = b + str(i)

    a = hashlib.sha3_224(h2.encode()).hexdigest()
    if a[0:2] == '01' and a[-2:] == '10':

        c = c + 1
        print(i)
        print('sha3_224')
        print(a)
    a = hashlib.sha3_256(h2.encode()).hexdigest()
    if a[0:2] == '01' and a[-2:] == '10':

        c = c + 1
        print(i)
        print('sha3_256')
        print(a)
    a = hashlib.sha3_384(h2.encode()).hexdigest()
    if a[0:2] == '01' and a[-2:] == '10':

        c = c + 1
        print(i)
        print('sha3_384')
        print(a)
    a = hashlib.sha3_512(h2.encode()).hexdigest()
    if a[0:2] == '01' and a[-2:] == '10':
        print(i)
        c = c + 1
        print('sha3_512')
        print(a)

print(b)


print(c)
