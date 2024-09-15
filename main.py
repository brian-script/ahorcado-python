import random

print("****Juego Ahorcado****\n")

intentos = 0

with open("diccionario.txt", "r") as archivo:
    palabra = archivo.readlines()
    #eturn palabra
print(random.choice(palabra).strip())

while intentos < 6:
    intentos = intentos + 1
    print(intentos)

