date1 = int(input("ingrese un numero: "))
date2 = int(input("ingrese un numero: "))
date3 = int(input("ingrese un numero: "))
date4 = int(input("ingrese un numero: "))
date5 = int(input("ingrese un numero: "))

datelist = [date1, date2, date4, date5]

if date3 > max(datelist):
    print("el tercer numero es el mayor")
else:
    print("el tercer numero no es el mayor")