class A:
    def _init_(self,x):
        self.x =x
        print("A init executed")
class B(A):
    def _init_(self):
        print("B init executed")
abc = B()
print(abc)
a = range(5)
it = iter(a)
print(next(it))
class syrange:
    def _init_(self,n):
        self.n 
    def _iniy_(self, myrange):
        self.myrange = myrange
        self.i = 0
for i in range(5):
    print(i)