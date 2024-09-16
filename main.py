import random

print("****Juego Ahorcado****\n")

intentos = 0

with open("diccionario.txt", "r") as archivo:
    palabra = archivo.readlines()

adivinar = random.choice(palabra).strip()

while intentos < 6:
    barra = " _ "
    frase = barra * len(adivinar)
    print(frase)
    letra = str(input("Agrega una letra: "))
    if letra in adivinar:
        print("Bien")
    else:
        intentos = intentos + 1
        print("Fallaste")





"""while intentos < 6:
    intentos = intentos + 1
    print(intentos)
"""


