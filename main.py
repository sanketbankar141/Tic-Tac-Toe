#--------- Global Variables -----------#

# Game Board
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_", ]

# if Game Is Still Going
game_still_going = True

# who won? or tie?
winner = None

# whos turn it is
current_player = 'X'

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# Play game of tic tac toe
def play_game():

#   display initial board
    display_board()

# While game is still going
    while game_still_going:
        handle_turn(current_player)

        # Check if game has ended
        check_if_game_over()

        # Flip to other player
        flip_player()


        # The game has ended
        if winner == "X" or winner == "O":
            print(winner + " won.")
        elif winner == None:
            print("Tie")



# Handle a single turn of an arbitory player
def handle_turn(player):

    print(player + "s turn.")
    position = input("choose a position from 1 to 9:")


    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("invalid input. Choose position from 1-9:")

        position = int(position) - 1

        if board[position] != "_":
            valid = True
        else:
            print("you cant go there. Go again.")

    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # set up global variable
    global winner

    # check_rows
    row_winner = check_rows()
    # check_columns
    column_winner = check_columns()
    # check_diagonals
    diagonal_winner = check_diagonals()

    # Get the Winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = columns_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return


def check_rows():
    # Set up global variable
    global game_still_going
    # check if any of the rows have all same value (and its not empty)
    row_1 = board[0] == board[1] == board[2] != '_'
    row_2 = board[3] == board[4] == board[5] != '_'
    row_3 = board[6] == board[7] == board[8] != '_'
    # If any of these have match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    #returned the winner ( X or O)
    if row_1:
       return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    # set up global variable
    global game_still_going
    # check if any of the rows have all same value (and its not empty)
    column_1 = board[0] == board[3] == board[6] != '_'
    column_2 = board[1] == board[4] == board[7] != '_'
    column_3 = board[2] == board[5] == board[8] != '_'
    # if any of these have match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # returned the winner ( X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    # set up global variable
    global game_still_going
    # check if any of the rows have all same value (and its not empty)
    diagonals_1 = board[0] == board[4] == board[8] != '_'
    diagonals_2 = board[6] == board[4] == board[2] != '_'
    # if any of these have match, flag that there is a win
    if diagonals_1 or diagonals_2:
        game_still_going = False
    # returned the winner ( X or O)
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return

def check_if_tie():
    if "_" not in board:
        game_still_going = False

    return



def flip_player():
    #global variables we need
    global current_player
    # if current player is X then change it to O
    if current_player == "X":
        current_player = "O"
    # if current player is O then change it to X
    elif  current_player == "O":
        current_player = "X"
    return


play_game()
#play game1
#handle turn
#check win
    #check rows
    #check columns
    #check diagonals
#check tie
#flip player
