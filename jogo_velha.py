board = [' ' for x in range(10)]  # lista vazia para o tabuleiro

def insert_letter(letter, pos):
    board[pos] = letter

def space_is_free(pos):
    return board[pos] == ' '

def print_board(board):
    #print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    #print('   |   |')
    #print('-----------')
    #print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    #print('   |   |')
    #print('-----------')
    #print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    #print('   |   |')

def is_winner(bo, le):
    return (
    (bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le)
    )

def player_move():
    run = True
    while run:
        move = input("Escolha uma posição para jogar (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print("Posição já ocupada!")
            else:
                print("Insira um número de 1 a 9!")
        except:
            print("Insira um número inteiro!")

def computer_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    corners = []
    for i in possible_moves:
        if i in [1,3,7,9]:
            corners.append(i)
    if len(corners) > 0:
        move = select_random(corners)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    edges = []
    for i in possible_moves:
        if i in [2,4,6,8]:
            edges.append(i)
    if len(edges) > 0:
        move = select_random(edges)

    return move

def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)

while True:
    print_board(board)
    player_move()
    comp = computer_move()
    print(comp)