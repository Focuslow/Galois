import galois
from sympy import Matrix, Symbol, S
import sympy
from SymbolE import AnticomSym
from FieldConstant import FieldConstant

def combine(poly1, poly2):
    x, y, z  = sympy.symbols('x,y,z')
    a, b, c  = sympy.symbols('a,b,c')
    #Substitute each variable x,y,z for another one a,b,c
    first = [poly1[0].subs({x:a, y: b, z: c}),poly1[1].subs({x:a, y: b, z: c})]
    #Substitute a,b,c for whole polynomials
    return [first[0].subs({a:poly2[0], b: poly2[1]}),first[1].subs({a:poly2[0], b: poly2[1]})]


def main():
    #Polynomial combination
    l1 = [2*x+y+1,x-y]
    t1 = [x+2*y**2,y+3]
    l2 = [x-4*y,2*x+y+2]

    print(*l1,sep='\n')
    print(*t1,sep='\n')
    print(*l2,sep='\n')
    print(*combine(t1,l2), sep='\n')

    #Matrix reversibility
    M = Matrix([[1, 0], [0, e]])
    print(M)
    print(M.det())
    print(M**-1)

    p = 31
    k = 1
    GF = galois.GF(p**k)
    
    a11 = FieldConstant(GF,3,10)
    a21 = FieldConstant(GF,7,5)
    a22 = FieldConstant(GF,9,3)
    t = [x+a11*y,y+3]
    l2 = [x-a21*y,a22*x**2+y+2]
    print(*t,sep='\n')
    print(*l2,sep='\n')
    print(*combine(t,l2), sep='\n')

if __name__ == "__main__":
    #Symbol initiation
    x, y, z  = sympy.symbols('x,y,z')
    e = AnticomSym('e')

    main()