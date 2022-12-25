a =5
print(isinstance(a,object))
class A:
    def _call_(self):
        print("You called me")
a = A
print(a)
class Exponent:
    def _init_(self,n):
        self.n = n
    def _getitem_(self,x):
        return x**self.n
e = Exponent(3)
print(e[6])