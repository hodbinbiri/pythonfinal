class abc:
    def __init__(self,x):
        self.x=x

    def multi(self,y):
        return(self.x*y)

myins=abc(5)
print(myins.multi(2))
