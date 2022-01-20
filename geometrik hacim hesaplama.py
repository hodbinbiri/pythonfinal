def hacimbul() :
    print("Girmek hesaplamak istediğiniz hacimin geometrik şeklini girin \n"
          "örn: Küp=kup,Diktörtgen Prizma=dp, Küre=kure")
    hesap = input("Hesaplamak isetdiğiniz geometrik şekli giriniz: ")

    if hesap == "kup" :
        a = int(input("bir kenar uzunluğunu girin: "))
        hacim= (a**3)
        return(hacim)

    elif hesap == "dp":
          a = int(input("a kenar uzunluğunu girin: "))
          b = int(input("b kenar uzunluğunu girin: "))
          c = int(input("c kenar uzunluğunu girin: "))
          hacim = (a*b*c)
          return(hacim)

    elif hesap == "kure" :
          r = int(input("r yarıçapını girin: "))
          hacim = ((4/3)*3.14*(r**3))
          return(hacim)

    else:
        print("Lütfen doğru geometrik şekil adı girin.")
        
print(hacimbul())
