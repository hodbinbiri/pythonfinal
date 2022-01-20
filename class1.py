class Ball:
    def __init__(self,color,size,weight,balltype):
        self.color=color
        self.size=size
        self.weight=weight
        self.balltype=balltype


    def bounce(self):
        if self.balltype.lower()=="bowling":
            print("Bowling balls cannot bounce")
        else:
            print(self.balltype, "ball bounces")

#b2=Ball("blue",4,3,"Bowling")
#print(b2.bounce())
