print("Tesoro vs Pirata")
print("(c) 2026")

jugador = 1

tablero = ["1", "2", "3",
           "4", "5", "6",
           "7", "8", "9"]

while True:

    print()
    print(tablero[0], "|", tablero[1], "|", tablero[2])
    print("---------")
    print(tablero[3], "|", tablero[4], "|", tablero[5])
    print("---------")
    print(tablero[6], "|", tablero[7], "|", tablero[8])

    posicion = int(input("Elige una casilla (1-9): ")) - 1

    if tablero[posicion] not in ["X", "O"]:

        if jugador == 1:
            tablero[posicion] = "G"
            jugador = 2
        else:
            tablero[posicion] = "🏴‍☠️"
            jugador = 1

    # Comprobar ganador
    combinaciones = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for c in combinaciones:
        if tablero[c[0]] == tablero[c[1]] == tablero[c[2]]:
            print()
            print("Tenemos ganador")
            print(tablero[c[0]], "ha ganado la partida")
            exit()