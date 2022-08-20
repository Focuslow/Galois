from sympy import Symbol, S

class AnticomSym(Symbol):
    def __new__(cls,*args,**kwargs):
        return super().__new__(cls,*args,**kwargs,commutative=False)

    def __mul__(self,other):
        if isinstance(other,AnticomSym):
            if other==self:
                return S.Zero
        return super().__mul__(other)

    def __pow__(self,exponent):
        if exponent>=2:
            return S.Zero
        else:
            return super().__pow__(exponent)