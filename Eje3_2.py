num = int(input("ingrese un numero: "))

acumulador = 1
cont = 1
while cont <= num:
    acumulador=acumulador * cont
    cont+=1
    print("el factorial es: ", acumulador)