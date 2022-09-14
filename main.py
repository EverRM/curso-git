#Tivia 

#declarando librerias
import random
import time

#declarando colores 

azul="\033[34m"
rojo="\033[31m"
reset="\033[39m"

  
puntaje=random.randint(0, 20)
participante=input("Bienvenido participante, como podemos nombrarte: ")
print(" *********************************")
print(participante +", Vamos a poner a prueba tus conocimientos")

print("sobre los componentes de una Pc\n")
print("selecciona tu respuesta escribiendo la letra de su alternativa y precionando ENTER para validar su respuesta\n")
print("Acumularas puntaje por cada respuesta correcta, "+"suerte.")
print("tu puntaje inicial es: ",puntaje)
print("---------------------------------- \n")
print("\n*******CARGANDO************\n") 

time.sleep(3)

#primera pregunta 

print("1-. Cual es el componente mas importante de una computadora\n")
print("A) memoria Ram")
print("B) Disco Duro")
print("C) Tarjeta Grafica")
print("D) CPU")


rta1=input("Escriba su respusta: ")

while rta1 not in("a","b","c","d","A","B","C","D"):
 rta1=input("\n*****************\nDebe insertar alguna de las alternativas\n*****************\n \nIntente Nuevamente: ")


if rta1 == "d":
  print(azul,"\nCorrecto ", reset)
  puntaje=puntaje+5

 
elif rta1 =="D":
  print(azul,"\nCorrecto ", reset)
  puntaje=puntaje+5
  

else: 
  print(rojo,"\nIncorrecto, descontaremos algunos puntos",reset)
  puntaje=puntaje-3
print("\n---------------------------------- \n")
#segunda pregunta

print("2-. componente electrónico que sirve para suministrar electricidad al computador\n")

print("A)  Fuente de poder ")
print("B)  memoria Ram")
print("C)  torre")
print("D)  mouse")



rta2=input("Escriba su respusta: ")

while rta2 not in("a","b","c","d","A","B","C","D"):
 rta2=input("\n*****************\nDebe insertar alguna de las alternativas\n*****************\n \nIntente Nuevamente: ")

if rta2 == "a":
  print(azul,"\nCorrecto ", reset)
  puntaje=puntaje+5

elif rta2 =="A":
  print(azul,"\nCorrecto ", reset)
  puntaje=puntaje+5

else: 
  print(rojo,"\nIncorrecto, descontaremos algunos puntos",reset)
puntaje=puntaje-2
print("\n---------------------------------- \n")

#tercera pregunta

print("3-. De los siguientes, cual es un dispositivo de salida.\n")

print("A)  Mouse ")
print("B)  Monitor")
print("C)  Microfono")
print("D)  Scaner")



rta3=input("Escriba su respusta: ")



while rta3 not in("a","b","c","d","A","B","C","D"):
 rta3=input("\n*****************\nDebe insertar alguna de las alternativas\n*****************\n \nIntente Nuevamente: ")

if rta3 == "b":
  print(azul,"\nCorrecto ", reset)
  puntaje=puntaje+5

elif rta3 =="B":
  print(azul,"\nCorrecto ", reset)
  puntaje=puntaje+5

else: 
  print(rojo,"\nIncorrecto, descontaremos algunos puntos",reset)
puntaje=puntaje-3
print("\n---------------------------------- \n")

#cuarta pregunta

print("4-. Son todos los componentes y dispositivos físicos de un computador.\n")

print("A)  Dispositivos de almacenamiento  ")
print("B)  Dispositivos de entrada")
print("C)  Hardware")
print("D)  Software")



rta4=input("Escriba su respusta: ")



while rta4 not in("a","b","c","d","A","B","C","D"):
 rta4=input("\n*****************\nDebe insertar alguna de las alternativas\n*****************\n \nIntente Nuevamente: ")


if rta4 == "c":
  print(azul,"\nCorrecto ", reset)
  puntaje=puntaje+5
  

   

elif rta4 =="C":
  print(azul,"\nCorrecto ", reset)
  puntaje=puntaje+5
  

else: 
  print(rojo,"\nIncorrecto, descontaremos algunos puntos",reset)
puntaje=puntaje-1

print("\n*******************\n") 

print("\n*******PROCESANDO************\n") 

time.sleep(3)
 

print("gracias por participar",participante,"tu puntaje total es de", puntaje, "puntos\n")

print("* * * * * * * * * * * * *" )
print(" * * * * * * * * * * * *")
print("\n*******Cerrando Trivia************\n") 
print("\n*******Esperamos su Regreso************\n")          
