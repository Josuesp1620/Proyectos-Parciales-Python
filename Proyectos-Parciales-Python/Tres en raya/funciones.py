import random
def gana_user():
    print("""
                    ¡Felicidades!
            o===========================o
            |     Usted ha ganado!!     |
            o===========================o""")

def gana_computer():
        print("""
                ¡Ha sido derrotado!
          o===============================o
          |  La computadora ha ganado!!   |
          o===============================o""")

def tablero(board):
    for fila in range(len(board)):
        print("+"+"-------+"*3)
        print("|"+"       |"*3, end="\n|")
        for columna in range(len(board[0])):
            print("   "+str(board[fila][columna])+"   |",end="")
        print("\n|"+"       |"*3)
    print("+"+"-------+"*3)

def  computer_juega_1(board):
    board[1] [1] = "X"

#jugada del user
def jugadas_user(board, jugada_user):
    while True:
        if jugada_user >= 1 and jugada_user <= 3:
            jugada_user-=1
            if board[0][jugada_user] == "X" or board[0][jugada_user] == "O":
                print("\nEsa casilla esta ocupada\n")
                jugada_user=int(input("Ingrese otro numero: "))

            else:
                board[0][jugada_user]="O"
                tablero(board)
                break

        elif jugada_user >= 4 and jugada_user <= 6:
            jugada_user-=4
            if board[1][jugada_user] == "X" or board[1][jugada_user] == "O":
                print("\nEsa casilla esta ocupada\n")
                jugada_user=int(input("Ingrese otro numero: "))

            else:
                board[1][jugada_user]="O"
                tablero(board)
                break

        elif jugada_user >= 7 and jugada_user <= 9:
            jugada_user-=7
            if board[2][jugada_user] == "X" or board[2][jugada_user] == "O":
                print("\nEsa casilla esta ocupada\n")
                jugada_user=int(input("Ingrese otro numero: "))

            else:
                board[2][jugada_user]="O"
                tablero(board)
                break


def jugadas_computer(board, num_aleatorio):
    while True:
        if num_aleatorio >= 1 and num_aleatorio <= 3:
            num_aleatorio-=1
            if board[0][num_aleatorio] == "X" or board[0][num_aleatorio] == "O":
                num_aleatorio = random.choice(range(1,10))

            else:
                board[0][num_aleatorio]="X"
                tablero(board)
                break

        elif num_aleatorio >= 4 and num_aleatorio <= 6:
            num_aleatorio-=4
            if board[1][num_aleatorio] == "X" or board[1][num_aleatorio] == "O":
                num_aleatorio = random.choice(range(1,10))

            else:
                board[1][num_aleatorio]="X"
                tablero(board)
                break

        elif num_aleatorio >= 7 and num_aleatorio <= 9:
            num_aleatorio-=7
            if board[2][num_aleatorio] == "X" or board[2][num_aleatorio] == "O":
                num_aleatorio = random.choice(range(1,10))

            else:
                board[2][num_aleatorio]="X"
                tablero(board)
                break