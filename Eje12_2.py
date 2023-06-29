ram = int(input("Ingrese un número: "))

acumulador = 0
num = 0
while num <= ram:
    acumulador=acumulador + num
    num+=2
    print("el acumulador es: ", acumulador)