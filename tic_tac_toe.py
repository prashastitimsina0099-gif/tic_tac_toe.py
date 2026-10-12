import math

# Tic-Tac-Toe with AI using Minimax

HUMAN = "X"
COMPUTER = "O"
EMPTY = " "

board = [EMPTY] * 9


def display_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i + 3]))
        if i < 6:
            print("---+---+---")
    print()


def check_winner(player):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def is_draw():
    return EMPTY not in board and not check_winner(HUMAN) and not check_winner(COMPUTER)


def minimax(is_maximizing, depth=0):
    if check_winner(COMPUTER):
        return 10 - depth

    if check_winner(HUMAN):
        return depth - 10

    if EMPTY not in board:
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == EMPTY:
                board[i] = COMPUTER
                score = minimax(False, depth + 1)
                board[i] = EMPTY
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(True, depth + 1)
                board[i] = EMPTY
                best_score = min(best_score, score)

        return best_score


def computer_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = COMPUTER
            score = minimax(False, 0)
            board[i] = EMPTY

            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = COMPUTER
        print("Computer chooses position:", best_move + 1)


def human_move():
    while True:
        try:
            position = int(input("Enter a position (1-9): ")) - 1

            if position < 0 or position > 8:
                print("Invalid position! Choose a number from 1 to 9.")
            elif board[position] != EMPTY:
                print("That position is already occupied. Try again.")
            else:
                board[position] = HUMAN
                break

        except ValueError:
            print("Please enter a valid number.")


def play_game():
    print("================================")
    print("     TIC-TAC-TOE WITH AI")
    print("================================")
    print("You are X, and the computer is O.")
    print("Choose a position using numbers 1-9.")
    print()
    print("Position guide:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")

    display_board()

    while True:
        human_move()
        display_board()

        if check_winner(HUMAN):
            print("Congratulations! You win!")
            break

        if is_draw():
            print("It's a draw!")
            break

        computer_move()
        display_board()

        if check_winner(COMPUTER):
            print("Computer wins! Better luck next time.")
            break

        if is_draw():
            print("It's a draw!")
            break

    print("Thanks for playing Tic-Tac-Toe!")


if __name__ == "__main__":
    play_game()
