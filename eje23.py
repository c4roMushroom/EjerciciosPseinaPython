num1 = int(input("ingrese un número: "))

if 1000 > num1 > 99 :
    if num1 % 2 == 0:
        print("el numero es par de tres digitos")
    else:
        print("el numero es impar de tres digitos")
else:
    print("el numero no es de tres digitos, vuelva a ingresar otro")  