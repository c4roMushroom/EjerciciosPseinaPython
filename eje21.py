num1 = int(input("ingrese un número: "))

if 100 > num1 > 9 :
    if num1 % 2 == 0:
        print("el numero es par de dos digitos")
    else:
        print("el numero es impar de dos digitos")
else:
    print("el numero no es de dos digitos, vuelva a ingresar otro")  