num = int(input("ingrese un numero: "))
 
x = 1
contador = 0
while x <= num:
    if num % x == 0: 
        contador = contador + 1  
    x = x+1
if contador == 2:
    print("el",num,"es primo")       
else:
    print("el",num,"no es primo")     