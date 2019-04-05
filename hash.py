n = int(input())
m = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]

def hashFirst(a):
    h=0
    b = str(abs(a))
    for i in range(len(b)):
        h=h+(h+int(b[i]*m[i]))*m[i]-m[i]
    return h
print(hashFirst(n))

m2 = 666

def hashSecond(a):
    h=0
    b = str(abs(a))
    for i in range(len(b)):
        h=h*m2+int(b[i])
    return h
print(hashSecond(n))

