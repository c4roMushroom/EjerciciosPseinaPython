num = int(input("ingrese un numero: "))

for par in range(1,num):
    if par % 2 == 1:
        print("Impares del 1 hasta el",num,": ",par)