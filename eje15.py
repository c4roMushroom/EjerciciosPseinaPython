word = input("ingrese una palabra: ")

l = 0

for i in word:
    l+=1
if l < 5:
    print("la longitud es menor de 5 caracteres")  
else:
    print("la longitud es mayor de 5 caracteres") 