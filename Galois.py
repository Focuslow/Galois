from cmath import inf
from venv import create
import galois
import time
import numpy as np
from tabulate import tabulate

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

def create_sumtable(points):
    col_names = []
    for i in points:
        col_names.append(str([j.tolist() for j in i]))
    col_names.insert(0,"+")
    rows = []
    for p in points:
        rows.append([i.tolist() for i in p])
        for q in points:
            rows[points.index(p)].append(sum_points(p,q))
    return tabulate(rows,headers=col_names,tablefmt="fancy_grid")


# #Large field generation with irreducible lookup table
# start = time.time()
# p=5
# k=10
# GF = galois.GF(p**k)
# field_str = str(p)+"^"+str(k)
# print(f"Galois field F{field_str} generation took "+str(time.time()-start)+" seconds")

# #Large field with calculated irreducible poly
# start = time.time()
# poly=galois.irreducible_poly(p,k)
# GF = galois.GF(p**k, poly)
# print(f"Galois field with irreducible poly F{field_str} generation took "+str(time.time()-start)+" seconds")
# print(GF(1589)+GF(65896))

# #F8 5+6=3
# GF8 = galois.GF(2**3)
# print(GF8(5)+GF8(6))

# #F4 2*3=1
# GF8 = galois.GF(2**2)
# print(GF8(2)*GF8(3))

# #2^1025 mod 511
# print(pow(2,1025,511))

# #print(GF.properties)
# #print(GF1.properties)

# GFtest = galois.GF(173**2,[1,0,2])
# GFtest1 = galois.GF(173**2)
# #a=galois.irreducible_poly(173**2,2)
# print(GFtest1.properties)
# print(GFtest(1000)*GFtest(2000))

#Poly test
GF5 = galois.GF(5**1)
GF16 = galois.GF(2**4)
# p=galois.Poly([1, 0, 3, 2], field=GF5)

p = 29
k = 1
GF = galois.GF(p**k)

# ECC definition
a = 4
b = 20
GFp=galois.Poly([1, 0, a, b], field=GF)

#check determinant
det = -16*(4*a**3+27*b**2)

if det%p == 0:
    raise Exception("Determinant of ECC is equal to 0")

p1 = galois.Poly([8, 3, 0, 2, 1], field=GF16)
p2 = galois.Poly([7, 0, 2, 0, 3, 3], field=GF16)
p3 = p1*p2
# print(p3)
# print(GFp)

residues = GF.quadratic_residues
print(f"Quadratic residues: {residues}")

roots = np.sqrt(residues)
print(f"Square roots of redisues {roots,-roots}")

points = [[np.full(1,np.inf), np.full(1,np.inf)]]
for i in range(29):
    print(i,": GF poly =",GFp(i))
    if GFp(i) in residues:
        root = roots[int(np.where(residues == GFp(i))[0])]
        points.append([GF(i), root])
        points.append([GF(i), -root])

print(points)
print(len(points))

# print (points[12], points[26])
# print(sum_points(points[12],points[26]))
# print(sum_points(points[0],points[26]))
# print(double_point(points[12]))
# print(create_sumtable(points))



