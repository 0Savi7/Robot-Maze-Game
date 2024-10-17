



def move_player(board,pos,lost):
    won = False
    if lost != True:
        move = input('which direction do you want to move? (upwards - 1, downwards - 2, left - 3, right - 4): ' )
        temp = []
        

        if pos != [0,4]:
            if move == '1':
                if board[pos[0]-1][pos[1]] == '-' or board[pos[0]-1][pos[1]] == '| ':
                    print()
                    print( 'You cant go up theres an obstacle blocking you!')
                elif board[pos[0]-1][pos[1]] == 0:
                    board[pos[0]-1][pos[1]] = '#'
                    board[pos[0]][pos[1]] = 0
                    temp = [pos[0]-1,pos[1]]
                    pos = temp
                    
            elif move == '2':
                if pos[0] == 9 or board[pos[0]+1][pos[1]] == '-' or board[pos[0]+1][pos[1]] == '|':
                    print()
                    print('You cannot go any further downwards!')
                else:
                    board[pos[0]+1][pos[1]] = '#'
                    board[pos[0]][pos[1]] = 0
                    temp = [pos[0]+1,pos[1]]
                    pos = temp

            elif move == '3':
                if pos[1] == 0 or board[pos[0]][pos[1]-1] == '|' or board[pos[0]][pos[1]-1] == '-':
                    print()
                    print('You cannot go any further to the left!')
                else:
                    board[pos[0]][pos[1]-1] = '#'
                    board[pos[0]][pos[1]] = 0
                    temp = [pos[0],pos[1]-1]
                    pos = temp
                    
            elif move == '4':
                if pos[1] == 9 or board[pos[0]][pos[1]+1] == '|' or board[pos[0]][pos[1]-1] == '-':
                    print()
                    print('You cannot go any further to the right!')
                else:
                    board[pos[0]][pos[1]+1] = '#'
                    board[pos[0]][pos[1]] = 0
                    temp = [pos[0],pos[1]+1]
                    pos = temp
            else:
                print()
                print('The value you have entered is not correct!')

        else:
            print()
            print('NICE YOU HAVE WON')
            won = True
        


    
    return pos , board , won
