import os
file=open("data3.txt", "w")
for n in range(5):
    cv=input("please enter next name")
    file.write(cv+ "\n")
file.close()

file=open("data3.txt","r")
print(file.read())

