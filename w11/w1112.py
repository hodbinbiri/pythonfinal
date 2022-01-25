class ball:
    def __init__(self,color,balltype):
        self.color=color
        self.balltype=balltype

    def bounce(self):
        if self.balltype=="Bowling":
            print("bowling balls do not bounce")

class C2(ball):
    def roll(self):
        print("you are rolling a", self.color,self.balltype, "ball")

x=C2("red","Bowling")

#x.roll()
#x.bounce()
