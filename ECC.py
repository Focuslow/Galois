from cmath import inf
import galois
import numpy as np
import math
import random

def sum_points(p, q):
    if p == q:
        return double_point(p)
    x1, x2, y1, y2 = p[0], q[0], p[1], q[1]

    if inf in p:
        x3 = x2
        y3 = y2
    
    elif inf in q:
        x3 = x1
        y3 = y1

    else:
        try:
            x3 = np.square((y2-y1)/(x2-x1))-x1-x2
            y3 = ((y2-y1)/(x2-x1))*(x1-x3)-y1
        except ZeroDivisionError:
            return [np.full(1,np.inf), np.full(1,np.inf)]

    return [x3,y3]

def double_point(p):
    x1,y1 = p[0], p[1]
    
    try:
        x3 = np.square((3*np.square(x1)+GF(a))/(2*y1))-2*x1
        y3 = ((3*np.square(x1)+GF(a))/(2*y1))*(x1-x3)-y1
    except ZeroDivisionError:
            return [np.full(1,np.inf), np.full(1,np.inf)]

    return [x3,y3]

p = 229
k = 1
GF = galois.GF(p**k)

# ECC definition
a = 4
b = 20
GFp=galois.Poly([1, 0, a%(pow(p,k)) , b%(pow(p,k))], field=GF)

#check determinant
det = -16*(4*a**3+27*b**2)

if det%p == 0:
    raise Exception("Determinant of ECC is equal to 0")

residues = GF.quadratic_residues
#print(f"Quadratic residues: {residues}")

roots = np.sqrt(residues)
#print(f"Square roots of redisues {roots,-roots}")

points = [[np.full(1,np.inf), np.full(1,np.inf)]]
for i in range(pow(p,k)):
    #print(i,": GF poly =",GFp(i))
    if GFp(i) in residues:
        root = roots[int(np.where(residues == GFp(i))[0])]
        points.append([GF(i), root])
        if root != 0:
            points.append([GF(i), -root])

#print(points)
print(len(points))

def encode(P,key,msg):
    sum_q = P
    rank = 1
    while sum_q[0] != inf and sum_q[1] != inf:
        sum_q = sum_points(sum_q,P)
        rank +=1
    Q = P
    a = random.randint(1,rank-1)
    doubles = math.floor(math.log(k,2))
    for i in range(doubles):
        Q = double_point(Q)

    for i in range(key-pow(2,doubles)):
        Q = sum_points(Q,P)

    m = points[msg]

    code1 = points[0]
    code2 = points[0]
    for i in range(a):
        code1 = sum_points(code1,P)
        code2 = sum_points(code2,Q)

    code2 = sum_points(m,code2)

    return [code1,code2]

def decode(msg,key):
    C1 = msg[0]
    C2 = msg[1]
    kC1 = C1
    doubles = math.floor(math.log(k,2))
    for i in range(doubles):
        kC1 = double_point(kC1)

    for i in range(key-pow(2,doubles)):
        kC1 = sum_points(kC1,C1)

    kC1[1]=-kC1[1]

    M = sum_points(C2,kC1)
    return M


msg = 'jozkomrkvicka'
msg = [ord(i)-96 for i in msg.lower()]
ascii_code = [i for i in range(97,122)]
P = points[8]
k = 262145
encoded = []
decoded = []
for i in msg:
    encoded.append(encode(P,k,i))

print(encoded)

for i in encoded:
    decoded.append(decode(i,k))

out_msg = ''
for i in decoded:
    out_msg+=str(chr(points.index(i)+96))

print(out_msg)
