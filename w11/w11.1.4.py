class Time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second

    def printtime(self):
        print("The time is %.2d : %.2d : %.2d" % (self.hour,self.minute,self.second))

t=Time(1,35,12)
t.printtime()

#%d yerine %.2d yazmamızın nedeni 01 02 diye göstresin diye.
