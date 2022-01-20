#----------------------------------------------------------------------------------------------------------------------
#WEEK8  - VERİ OLUŞTURMA -
#x="a","b","c"
#print(x)
#print(type(x))

#--- "," koyunca tuple olarak algılıyor, koymazsn str olarak algılar
#x="a"
#print(x)
#print(type(x))

#x="a",
#print(x)
#print(type(x))

#x=tuple("James")
#print(x[2])
#print(x[3])
#print(x[1:4])
#print(x[:])
#not: [] fonksiyonu sıralama yapıyor ör: 1:3   birden üçe kadar tüm veriler üç dahil değil.
#print(x[1:3])

#Veri Değiştirme
#x=4
#y=2
#temp=x
#x=y
#y=temp
#print(x,y)

#x=tuple("arif")
#y=tuple("emre")
#print(x+y)
#x,y=y,x
#print(x+y)

#x="emresevil22@icloud.com"
#print(x)
#username,domain=x.split("@")
#print(username)
#print(domain)
#a,b=x.split(".")
#print(a)
#print(b)
#print(a+b)
#print(a,b)

#MOD hesaplama kodu
#x=divmod(14,3)
#print(x)

#HEX TABANI İLE SAYILARI GÖSTERME
#print(hex(61))
#print(hex(16))
#print(hex(140))
#print(16*8+12)

#x="0x1a"
#y=int(x,16)
#print(y)

#a="0xff"
#b=int(a,16)
#print(b)
#print(16*15+15)

#BASİT BİR SAYIYI HEX TABANLI YAZMA MAKİNESİ
#program1
#def calculator():
#    number=(input("please you write an number"))
#    while int(number)>0:
#          hesaplama=hex(int(number))
#         return(hesaplama)

#print(calculator())

#---------------------------------
#program2

#def program(number):
#    a= "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "f"
#    hp=divmod(number,16)
#    print("Program:", "0x"+ a[hp[0]] + a[hp[1]])
#v=int(input("enter a number"))
#program(v)
#print("Python:", hex(v))
#--------------------------------

#x="abc"
#y=[0,1,2]
#print(zip(x,y))
#for p in zip(x,y):
    #print(p)
#print(list(zip(x,y)))

#x={"a":1, "b":3, "r":5}
#z=x.items()
#print(z)


#----------------------------------------------------------------------------------------------------------------------
#WEEK 9

#x="abc"
#y="xy"
#for l in x:
    #print(x)

#for b in x:
    #print(b)

#for w in x:
    #print(w+y)
    #print(list(w))
#print(list(x))

#class Ball:
#    def __init__(self,color,size,weight):
#        self.color=color
#        self.size=size
#        self.weight=weight
#b=Ball("red",13,31)
#print(b.size)
#print(b.color)
#init = başlangıç, birim demek. uni kullanarak bir fonksiyon oluşturuyoruz. -Class sınıf , b olarak oluşturuduğumuz bir nesne, self ve __init__ i kulllanmak zorundayız.

#OS MODÜLÜ
#import os
#print(os.name)  #işletim sisteminin değerini döndürür

#print(os.sep)   #işletim sisteminin ayracının hangi gösterimde olduğunu gösterir

#print(os.getcwd())  #bulunduğum dosyanın nerede olduğunu gösteriyor

#print(os.listdir(r'/Users/emresevil/PycharmProjects/pythonProject/venv'))

#liste=(os.listdir(os.getcwd()))
#for i in liste:
    #print(i)

#os.remove("deneme.txt)  #dosyayı siler

#class Ball:
#    def __init__(self,color,size,weight,balltype):
#        self.color=color
#        self.size=size
#        self.weight=weight
#        self.balltype=balltype


#    def bounce(self):
#        if self.balltype.lower()=="bowling":
#            print("Bowling balls cannot bounce")
#        else:
#            print(self.balltype, "ball bounces")

#b2=Ball("blue",4,3,"Bowling")
#print(b2.bounce())

#class calculate:
#    def add(self,number1,number2):
#        return(number1+number2)

#    def mult(self,number1,number2):
#        return (number1 * number2)

#    def min(self,nr1,nr2):
#        return(nr1-nr2)

#x=calculate()
#print(x.add(1,3))
#print(x.mult(3,5))
#print(x.min(3,10))

#k=[1,3,4,5,6,7,"a"]
#for n in k:
#    print(n)

#username=input("please enter your name")
#print("Hello" , username)
#k=[12,23,34]
#k[1]="23456"
#print(k[0])
#print(k[1])
#print(k[2])

#-----------------------------------------------------------------------------------------------------------------------
#WEEK 10

#s="emre"
#print(s)
#print(type(s))
#print(len(s))
#u="emre piton sınavından yüksek almak istiyor"
#print(len(u))
#print(u)
#print(len(u)-1)
#print(42)
#print(u[1])
#print(u[1:9])
#print(u[-1])
#print(u[-4])
#print(u[:3])
#print(u[:])

#for x in u:
#    print(x)

#x="XWYZ"
#y="uuu"
#for p in x:
    #print(x+y)
    #print(p)
    #print(p+y)

#x="MERHABA"
#print(x.lower())
#print(x.find("A"))

#x="Hello"
#print(x.upper())
#print(x.find("l"))
#print(x.find("el"))
#print(x.find("l",3))
#print(x.find("x"))

#print("x" in "Hello")
#print("e" in "Hello")

#print("the valuse is %d" %5)

# %d = int , #g = float
#x=1.25
#print("the coef is %g" %x)
#print("the coeff is %d" %1.24)
