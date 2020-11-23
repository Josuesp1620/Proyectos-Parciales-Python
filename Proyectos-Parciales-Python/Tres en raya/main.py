import random
from funciones import gana_user,gana_computer,tablero,computer_juega_1,jugadas_user,jugadas_computer
board = [[1,2,3],[4,5,6],[7,8,9]] 
print("""
            o===========================o
            |   Bienvenido a mi juego!  |
            o===========================o
""")

name=input("""
            Ingrese su nombre: """)

print(f"""
            ¡Bien {name}, A JUGAR!
""")
turno=0
inicio_juego = 0
computer_juega_1(board)
tablero(board)

while turno < 8:
        
    if inicio_juego == 0:
        turno += 1
        inicio_juego += 1
        # Turno del jugador
        print("\n Escoja un numero del 1  - 9! ")
        print("  Es tu turno! \n")
        jugada_user=int(input("Ingrese su numero: "))
        jugadas_user(board, jugada_user)

        if True:
            if board[0][0] == "O" and board[0][1]== "O" and board[0][2] == "O":
                gana_user()
                break
            elif board[1][0] == "O"and board[1][1]== "O" and board[1][2] == "O":
                gana_user()
                break
            elif board[2][0] == "O" and board[2][1]== "O" and board[2][2] == "O":
                gana_user()
                break
            elif board[2][0] == "O" and board[1][1]== "O" and board[0][2] == "O":
                gana_user()
                break
            elif board[0][0] == "O" and board[1][0]== "O" and board[2][0] == "O":
                gana_user()
                break
            elif board[0][1] == "O" and board[1][1]== "O" and board[2][1] == "O":
                gana_user()
                break
            elif board[0][2] == "O" and board[1][2]== "O" and board[2][2] == "O":
                gana_user()
                break

    elif inicio_juego == 1:
        # Turno de la computadora
        turno += 1
        inicio_juego -= 1
        print("\n Turno de la computadora! \n")
        num_aleatorio = random.choice(range(1,10))  
        jugadas_computer(board, num_aleatorio)
        if True:
            if board[0][0] == "X" and board[0][1]== "X" and board[0][2] == "X":
                gana_computer()
                break
            elif board[1][0] == "X" and board[1][1]== "X" and board[1][2] == "X":
                gana_computer()
                break
            elif board[2][0] == "X" and board[2][1]== "X" and board[2][2] == "X":
                gana_computer()
                break
            elif board[2][0] == "X" and board[1][1]== "X" and board[0][2] == "X":
                gana_computer()
                break
            elif board[0][0] == "X" and board[1][0]== "X" and board[2][0] == "X":
                gana_computer()
                break
            elif board[0][1] == "X" and board[1][1]== "X" and board[2][1] == "X":
                gana_computer()
                break
            elif board[0][2] == "X" and board[1][2]== "X" and board[2][2] == "X":
                gana_computer()
                break
if turno == 8:
    print("""
             EL juego ha quedado empate!""")

print("""
            o===========================o
            |  Gracias hasta la proxima |
            o===========================o
""")