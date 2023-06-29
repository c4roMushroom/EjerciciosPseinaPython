word = input("ingrese una palabra: ")

l = 0

for i in word:
    l+=1
if l > 10:
    print("la longitud es mayor a 10 caracteres")  
else:
    print("la longitud es menor a 10 caracteres") 