num = int(input("digite un numero: "))

suma = 0
while num>0:
    suma = suma + (num % 10)
    num = num//10
print("la suma de los digitos es: ",suma)