class abc:
    def __init__(self,a):
        self.a=a

    def findtotal(self,b):
        res=self.a+b
        return res

#x=abc(5)
#print(x.findtotal(3))


    def multi(self,b):
        res=self.a*b
        return res
x=abc(7)
print(x.multi(3))





