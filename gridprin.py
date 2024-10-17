def grid(board):
    row = ''
    print()
    print()
    print()
    for i in range(len(board)):
        for j in range(len(board[i])):
            row += ' ' + str(board[i][j])
        print(row)
        row = ''