num = int(input("ingrese un numero: "))

for par in range(1,num):
    if par % 2 == 0:
        print("Pares del 1 hasta el",num,": ",par)