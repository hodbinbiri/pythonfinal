import os
file=open("data2.txt","w")
for n in range(5):
    cv=input(" please enter next name ")
    file.write(cv)
file.close()
