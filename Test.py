from sympy import Symbol, S
import sympy
import galois

class Test(sympy.Number):

    def __new__(self,gf,a,b,*args,**kwargs):
        self.GF = galois.GF(gf)
        self.a = self.GF(a)
        self.b = self.GF(b)
        return self

    def __init__(self, gf, a, b, name) -> None:
        self.GF = galois.GF(gf)
        self.a = self.GF(a)
        self.b = self.GF(b)
        self.name = name


    def __mul__(self,other):
        if isinstance(other,Test):
            if other==self:
                return S.Zero
        return super().__mul__(other)

    def __add__ (self,other):
            if isinstance(other,Test):
                a = self.a + other.a
                b = self.b + other.b
                return Test(self.GF.order, a, b, self.name)
            else:
                return super().__sum__(other)

    def __radd__(self,other):
          return self.__add__(other)

    def __str__(self):
        string = f"({self.a}+{self.b}e)"
        return string

    def __pow__(self,exponent):
        if exponent>=2:
            return S.Zero
        else:
            return super().__pow__(exponent)

a11 = Test(31,3,10,1)
b11 = Test(31,7,30,1)
x, y, z  = sympy.symbols('x,y,z')

g=a11*y
print(g)