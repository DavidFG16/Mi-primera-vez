 #Variables
name = "David Gamboa" #variable String
age = 24 #numero entero
heigth = 1.63 #numeros decimales 
trainer = True #datos booleanos

#Conjunto de datos
hobbies = list() #Declaro variable
hobbies = ["cocinar","programar","dormir","Música"] #Vector, inicializo variable
print(hobbies)

#Operadores lógico

edad = int(input("Ingrese su edad: "))

if(edad == 17):
    print("Puede solicitar un crédito como pasante")
elif(edad >= 18 and edad < 20):
    print("Puede solicitar un crédito")
elif(edad >=20 and edad <= 24):
    print("Puede solicitar un crédito y bono")
else:
   print("No puede solicitar un crédito")
