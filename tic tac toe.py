import random

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerInput(board):
    while True:
        inp = input("Select a spot 1-9: ")
        if inp.isdigit():
            inp = int(inp)
            if 1 <= inp <= 9 and board[inp - 1] == "-":
                return inp - 1
            else:
                print("Invalid spot or spot already taken.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")


def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True

def checkIfWin(board, player_name):
    if checkHorizontal(board) or checkRow(board) or checkDiag(board):
        printBoard(board)
        if winner == "X":
            print(f"Congratulations, {player_name}! You win!")
        else:
            print("Computer wins!")
        return True
    return False

def checkIfTie(board):
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        return True
    return False

def switchPlayer(currentPlayer):
    return "O" if currentPlayer == "X" else "X"

def computer_move(board):
    while True:
        position = random.randint(0, 8)
        if board[position] == "-":
            return position

def main():
    print("Welcome to Tic Tac Toe!")
    player_name = input("Enter your name: ")

    while True:
        print(f"Hello, {player_name}! You are 'X' and the computer is 'O'.")
        board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        currentPlayer = "X"
        winner = None
        gameRunning = True
        player_positions = []
        computer_positions = []

        while gameRunning:
            if currentPlayer == "X":
                printBoard(board)
                position = playerInput(board)
                board[position] = currentPlayer
                player_positions.append(position)
            else:
                position = computer_move(board)
                board[position] = currentPlayer
                computer_positions.append(position)

            if checkIfWin(board, player_name):
                printBoard(board)
                break

            if checkIfTie(board):
                printBoard(board)
                break

            currentPlayer = switchPlayer(currentPlayer)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

main()