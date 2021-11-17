board = [" "] * 9
def draw_board(board):
    row_1 = "{}|{}|{}".format(board[0],board[1],board[2])
    row_2 = "{}|{}|{}".format(board[3],board[4],board[5])
    row_3 = "{}|{}|{}".format(board[6],board[7],board[8])

    print(row_1+'\n'+row_2+'\n'+row_3)

def user_move(board, user_type):
    user_choice = int(input('Choose your space between 1-9: ')) -1
    if board[user_choice] != ' ':
        print('Space is already Taken, please try again! ')
        user_move(board, user_type)
    else:
        board[user_choice]=user_type

def check_win(board, x_o):
    if board[0] == x_o and board[1] == x_o and board[2] == x_o or board[3] == x_o and board[4] == x_o and board[5] == x_o or board[6] == x_o and board[7] == x_o and board[8] == x_o or board[0] == x_o and board[3] == x_o and board[6] == x_o or board[1] == x_o and board[4] == x_o and board[7] == x_o or board[2] == x_o and board[5] == x_o and board[8] == x_o or board[0] == x_o and board[4] == x_o and board[8] == x_o or board[2] == x_o and board[4] == x_o and board[6] == x_o:
        play=False
    else:
        play=True
    return play

board = [" "] * 9
draw_board(board)
while 1==1:
    user_move(board, 'x')
    draw_board(board)
    user_move(board, 'o')
    draw_board(board)
