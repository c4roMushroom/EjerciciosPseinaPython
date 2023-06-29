date1 = int(input("ingrese un numero: "))
date2 = int(input("ingrese un numero: "))
date3 = int(input("ingrese un numero: "))
date4 = int(input("ingrese un numero: "))
date5 = int(input("ingrese un numero: "))

datelist = [date1, date2, date3, date4, date5]

esp = int(input("ingrese el numero que quiere buscar: "))

if esp in datelist:
    print("el numero esta en la lista")
else:
    print("el numero no esta en la lista. Busque otro:)")