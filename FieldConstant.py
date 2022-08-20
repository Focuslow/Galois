from SymbolE import AnticomSym
import sympy

class FieldConstant():
    def __init__(self, GF, a, b) -> None:
        self.GF = GF
        self.a = self.GF(a)
        self.b = self.GF(b)

    def __mul__(self,other):
        if isinstance(other,FieldConstant):
            if other==self:
                return sympy.S.Zero
        elif isinstance(other,sympy.core.mul.Mul):
            pass
        elif isinstance(other,sympy.core.symbol.Symbol):
            pass

    def __add__ (self,other):
        if isinstance(other,FieldConstant):
            return FieldConstant(self.GF, self.a+other.a, self.b+other.b)
        elif isinstance(other,int) or isinstance(other,float):
            return FieldConstant(self.GF, self.a+self.GF(other), self.b)
        elif isinstance(other,AnticomSym):
            return FieldConstant(self.GF, self.a, self.b+self.GF(other))
        elif isinstance(other,sympy.core.mul.Mul):
            for element in other.args:
                if isinstance(element ,AnticomSym):
                    return FieldConstant(self.GF, self.a, self.b+self.GF(int(other.args[0])))
        return super().__sum__(other)

    def __radd__(self,other):
          return self.__add__(other)

    def __str__(self):
        string = f"{self.a}+{self.b}e"
        return string