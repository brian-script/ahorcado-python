import random


def ascii(intentos):
    if intentos == 0:
        print("""
                  +------+
                  |      |
                         |
                         |
                         |
                         |
                 =========
              """)
    elif intentos == 1:
        print("""
                  +------+
                  |      |
                  O      |
                         |
                         |
                         |
                 =========
              """)
    elif intentos == 2:
        print("""
                  +------+
                  |      |
                  O      |
                  |      |
                         |
                         |
                 =========
              """)
    elif intentos == 3:
        print("""
                  +------+
                  |      |
                  O      |
                 /|      |
                         |
                         |
                 =========
              """)
    elif intentos == 4:
        print("""
                  +------+
                  |      |
                  O      |
                 /|\     |
                         |
                         |
                 =========
              """)
    elif intentos == 5:
        print("""
                  +------+
                  |      |
                  O      |
                 /|\     |
                 /       |
                         |
                 =========
              """)
    elif intentos == 6:
        print("""
                  +------+
                  |      |
                  O      |
                 /|\     |
                 / \     |
                         |
                 =========
              """)


print("****Juego Ahorcado****\n")

intentos = 0

with open("diccionario.txt", "r") as archivo:
    palabra = archivo.readlines()

adivinar = random.choice(palabra).strip()

progreso = ["_"] * len(adivinar)

ascii(intentos)
while intentos < 6 and "_" in progreso:

    print(" ".join(progreso))
    letra = str(input("Agrega una letra: "))

    if letra in adivinar:
        for i, l in enumerate(adivinar):
            if l in letra:
                progreso[i] = letra
    else:
        intentos = intentos + 1
        print("Fallaste")

    ascii(intentos)

if intentos == 6:
    print(f"la frase era {adivinar}")



