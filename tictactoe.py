'''
CSE210-01 Tic-Tac-Toe
Caleb Francis
'''

def main():
    board = [1,2,3,4,5,6,7,8,9]
    win_lose = 0
    turn_count = 1
    while win_lose == 0:
        show_board(board)
        if turn_count %2 == 1:
            player_turn("x", board)
            turn_count = turn_count + 1
        else:
            player_turn("o", board)
            turn_count = turn_count + 1
        win_lose = win(board)
        if turn_count == 10:
            win_lose = 2
    print()
    if win_lose == 1:
        print ("Congratulations, you won!")
    else:
        print("It was a tie!")
    print()
    

def show_board(board):
    print()
    print (f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print (f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print (f"{board[6]}|{board[7]}|{board[8]}")
    print()

def player_turn(turn, board):
    change = int(input(f"{turn}'s turn to choose a square (1-9): "))
    board [change-1] = turn
    return board
    
def win(board):
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        return 1
    return 0
'''
def tie(board):
    for count in range(9):
        if board[count] != "x" and board[count] != "o":
            return 2
    return 0
'''

main()
