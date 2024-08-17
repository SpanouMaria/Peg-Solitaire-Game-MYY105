# Peg Solitaire.
# Created in December 2021.
# Author Maria Spanou.

# Welcome message.
print('Welcome to peg solitaire!')

# Game Table visualization.
line1=[' ','','1','2','3','4','5','6','7']
line2=['A','',' ',' ','1','1','1',' ',' ']
line3=['B','',' ',' ','1','1','1',' ',' ']
line4=['C','','1','1','1','1','1','1','1']
line5=['D','','1','1','1','0','1','1','1']
line6=['E','','1','1','1','1','1','1','1']
line7=['F','',' ',' ','1','1','1',' ',' ']
line8=['G','',' ',' ','1','1','1',' ',' ']

# Game Table construction.
game_board=[line1, line2, line3, line4, line5, line6, line7, line8]

# Prints the current state of game table.
def board(game_board):
    for row in game_board:
        print(' '.join(row))

# Hundles the player's moves.
def move(game_board):
    if not has_valid_moves(game_board):
        print('No more moves, game ended!')
        return
    
    x = input('Enter peg position, followed by move (L,R,U or D): ')
    y = x.upper()
    m = list(y)

    notValid = not_valid(m)
    Valid = valid(m)

    if notValid==False or Valid==False:
       move(game_board)
    else:
        board(game_board)
        move(game_board)

# Position of character in the alphabet.
def char_position(char):
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 1
    else:
        return -1 
    
# Invalid game moves.
def not_valid(m):
    if (m[0] not in 'ABCDEFG') or (m[1] not in '1234567') or (m[2] not in 'LRUD'):
        print('Something wrong with your input, check again!')
        return False

    row = char_position(m[0])
    col = int(m[1])

    if (m[0] in 'ABFG') and ((col==3 and m[2]=='L') or (col==5 and m[2]=='R') or (col in [1, 2, 6, 7])):
        print('Invalid move, no peg!')
        return False

    if (col in [1, 2, 6, 7]) and ((m[0]=='E' and m[2]=='D') or (m[0]=='C' and m[2]=='U')):
        print('Invalid move, no peg!')
        return False

    if (col==1 and m[2]=='L') or (col==7 and m[2]=='R') or (m[0]=='A' and m[2]=='U') or (m[0]=='G' and m[2]=='D'):
        print('Out of board!')
        return False

    if game_board[row][col+1]=='0' or game_board[row][col+1]==' ':
        print('No peg in this position!')
        return False

    return True

# Valid game moves.
def valid(m):
    row = char_position(m[0])
    col = int(m[1])+1

    print(f"Checking validity of move: {m} (row {row}, col {col})")

    if m[2]=='L':
        if col > 2 and game_board[row][col]=='1' and game_board[row][col - 1]=='1' and game_board[row][col - 2]=='0':
            game_board[row][col] = '0'
            game_board[row][col - 1] = '0'
            game_board[row][col - 2] = '1'
            return True
    elif m[2]=='R':
        if col < 6 and game_board[row][col]=='1' and game_board[row][col + 1]=='1' and game_board[row][col + 2]=='0':
            game_board[row][col] = '0'
            game_board[row][col + 1] = '0'
            game_board[row][col + 2] = '1'
            return True
    elif m[2]=='U':
        if row > 2 and game_board[row][col]=='1' and game_board[row - 1][col]=='1' and game_board[row - 2][col]=='0':
            print(f"Checking positions: {game_board[row][col]} {game_board[row - 1][col]} {game_board[row - 2][col]}")
            game_board[row][col] = '0'
            game_board[row - 1][col] = '0'
            game_board[row - 2][col] = '1'
            return True
    elif m[2]=='D':
        if row < 6 and game_board[row][col]=='1' and game_board[row + 1][col]=='1' and game_board[row + 2][col]=='0':
            game_board[row][col] = '0'
            game_board[row + 1][col] = '0'
            game_board[row + 2][col] = '1'
            return True

    print("Move is not valid!")
    return False    
    
# Checks if there are any other valid moves for the player to make.
def has_valid_moves(game_board):
    for row in range(1, 8):
        for col in range(2, 8):
            if game_board[row][col]=='1':
                if col > 2 and game_board[row][col - 1]=='1' and game_board[row][col - 2]=='0':
                    return True
                if col < 6 and game_board[row][col + 1]=='1' and game_board[row][col + 2]=='0':
                    return True
                if row > 2 and game_board[row - 1][col]=='1' and game_board[row - 2][col]=='0':
                    return True
                if row < 6 and game_board[row + 1][col]=='1' and game_board[row + 2][col]=='0':
                    return True
    return False

# Counts the remaining pegs.
def remaining_pegs():
    y1=0
    for row in range(0,8):
        y1+=game_board[row].count('1')
    return y1

# If there are no more valid moves, the game ends.
def end_game():
    if not has_valid_moves(game_board):
        remaining_pegs()

# Main def.
def Game():
    board(game_board)
    move(game_board)
    end_game()

Game()