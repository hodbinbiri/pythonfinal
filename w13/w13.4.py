import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5,6,7,8]
y=[1,2,3,4,3,2,1,0]

plt.plot(x,y, "b")  #"b" grafik çizgisini değiştiriyor (rengini)
plt.xlabel("Inputs")
plt.ylabel("Steps")
plt.title("Constant Complexity")

plt.show()
