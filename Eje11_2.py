ram = int(input("Ingrese un número: "))

acumulador = 0
num = 1
while num <= ram:
    acumulador=acumulador + num
    num+=1
    print("el acumulador es: ", acumulador)