from numbers import Number
from numbers import Integral
class Polynomial:
    def __init__(self, coefs):
        self.coefficients = coefs  

    def degree(self):
        if isinstance(self.coefficients, tuple):
            return len(self.coefficients)-1
        else:
            return 0

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1]==1 else coefs[1]}x")
        terms += [f"{''if c == 1 else c}x^{d}"
                for d,c in enumerate(coefs[2:],start=2) if c]
        return " + ".join(reversed(terms)) or "0"
    def __eq__(self, other):
        return self.coefficients == other.coefficients
    def __add__(self, other):
        if isinstance(other, Polynomial):
            common = min(self.degree(),other.degree()) +1
            coefs = tuple(a+b for a,b in zip(self.coefficients,other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]
        elif isinstance(other,Number):
            return Polynomial((self.coefficients[0] + other,) + self.coefficients[1:])
        else: 
            return NotImplemented
        return Polynomial(coefs)
    def __radd__(self, other):
        return self + other 
    
    def __sub__(self, other):
        if isinstance(other,Polynomial):
            common = min(self.degree(),other.degree())+ 1
            coefs = tuple(a-b for a,b in zip(self.coefficients, other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]
        elif isinstance(other,Number):
            return Polynomial((self.coefficients[0] - other,) + self.coefficients[1:])
        else:
            return NotImplemented 
        return Polynomial(coefs)
    def __rsub__(self,other):
        return self - other
    def __mul__(self,other):
        if isinstance(other,Polynomial):
            t = Polynomial((0,0))
            for i in range(self.degree()+1):
                insertzeros = tuple([0 for n in range(i) ]) + other.coefficients
                multcoefs = tuple([insertzeros[l]*self.coefficients[i] for l in range(len(insertzeros))])
                t+= Polynomial(multcoefs)
            return t
        elif isinstance(other, Number):
            coefs = tuple([other * self.coefficients[i] for i in range(self.degree() +1)])
        else:
            return NotImplemented
        return Polynomial(coefs)    
    def __rmul__(self,other):
        return self*other
    def __pow__(self,other):
        if isinstance(other,Integral):
            t = Polynomial((1,0))
            for i in range(other):
                t = t*self
            return t
        else:
            return NotImplemented
    def __call__(self,other):
        if isinstance(other,Number):
            t = 0 
            for i in range(len(self.coefficients)):
                t += self.coefficients[i]*(other**i)
            return t
        else:
            return NotImplemented
    def dx(self):
        if self.degree() == 0:
            return 0
        elif isinstance(self,Number):
            return 0
        else:
            coefs = tuple([(i+1)*self.coefficients[i+1]for i in range(self.degree())])
            return Polynomial(coefs)

def derivative(x):
    return x.dx()
                   





            

