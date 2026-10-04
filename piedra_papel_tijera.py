import random
 
print("=== PIEDRA, PAPEL O TIJERA ===")
 
victorias = 0
derrotas = 0
empates = 0
 
jugar = "s"
 
while jugar == "s":  
 
    print("")
    print("Elige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    opcion = input("Tu opción (1-3): ")
 
    while opcion != "1" and opcion != "2" and opcion != "3":
        print("Opción no válida. Intenta de nuevo.")
        opcion = input("Tu opción (1-3): ")
 
    usuario = int(opcion)
 
    computador = random.randint(1, 3)
 
    if usuario == 1:
        print("Tú elegiste: Piedra")
    elif usuario == 2:
        print("Tú elegiste: Papel")
    else:
        print("Tú elegiste: Tijera")
 
    if computador == 1:
        print("El computador eligió: Piedra")
    elif computador == 2:
        print("El computador eligió: Papel")
    else:
        print("El computador eligió: Tijera")

    if usuario == computador:
        print("Resultado: ¡Empate!")
        empates = empates + 1
    else:

        if (usuario == 1 and computador == 3) or (usuario == 2 and computador == 1) or (usuario == 3 and computador == 2):
            print("Resultado: ¡Gana el usuario!")
            victorias = victorias + 1
        else:
            print("Resultado: Gana el bot.")
            derrotas = derrotas + 1
 
    jugar = input("\n¿Deseas jugar de nuevo? (s/n): ")
    while jugar != "s" and jugar != "n":
        print("Responde con 's' para sí o 'n' para no.")
        jugar = input("¿Deseas jugar de nuevo? (s/n): ")
 
print("")
print("--- Marcador final ---")
print("Victorias:", victorias)
print("Derrotas:", derrotas)
print("Empates:", empates)
print("Partida finalizada. ¡Gracias por jugar!")
 