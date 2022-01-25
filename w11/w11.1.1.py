class ball:
    def __init__(self,color,balltype):
        self.color=color
        self.balltype=balltype

    def bounce(self):
        if self.balltype=="Bowling":
            print("bowling balls do not bounce")

x=ball("red","Bowling")
x.bounce()

    
