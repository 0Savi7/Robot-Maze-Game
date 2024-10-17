from gridprin import grid

def check(board,posA,posP,lost):
    if posA[0]+1 == posP[0] and posA[1] == posP[1] :
        
        lost = True
    elif posA[0]-1 == posP[0] and posA[1] == posP[1] :
        
        lost = True
    elif posA[1]+1 == posP[1] and posA[0] == posP[0] :
        
        lost = True
    elif posA[1]-1 == posP[1] and posA[0] == posP[0] :
        
        lost = True

    return lost

    
def positions(board,posA,posP,lost):
    if lost != True:
        if posA[0] < posP[0]:
            board[posA[0]+1][posA[1]] = '%'
            board[posA[0]][posA[1]] = 0
            temp = [posA[0]+1,posA[1]]
            posA = temp

        elif posA[0] > posP[0]:
            board[posA[0]-1][posA[1]] = '%'
            board[posA[0]][posA[1]] = 0
            temp = [posA[0]-1,posA[1]]
            posA = temp

        elif posA[0] == posP[0]:

            if posA[1] < posP[1]:
                board[posA[0]][posA[1]+1] = '%'
                board[posA[0]][posA[1]] = 0
                temp = [posA[0],posA[1]+1]
                posA = temp

            elif posA[1] > posP[1]:
                board[posA[0]][posA[1]-1] = '%'
                board[posA[0]][posA[1]] = 0
                temp = [posA[0],posA[1]-1]
                posA = temp
    return board,posA,posP


         
