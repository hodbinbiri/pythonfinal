class abc:
    def __init__(self,a):
        self.a=a

    def findtotal(self,b):
        print(self.a, "plus", b, "is", (self.a+b))

x=abc(6)
x.findtotal(3)
