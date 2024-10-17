from Move import move_player
from gridprin import grid
from tester import positions
from tester import check

print("""
    WELCOME! to Savi's Epic prison maze escape. In this game you are a prisoner (the #) and you are being chased down by the
    gaurd ( the %). Your goal is to get to the entrance at the top of the maze without getting caught by the gaurd. You move by
    entering a number which corresponds to a certain movement, REMEBER entering a value thats not in the options can result in
    you loosing your turn, after all you are escaping a gaurd and any hestitaion or miscalculation on your part can get you
    caught. There will be walls : | or - which will be blocking your way remeber to avoid them at all costs since running into
    one can cause you an entire turn in which the gaurd will be able to come closer to you. Also a point you should remeber is
    unlike you the gaurd can move through walls. Anyways thats all from me I hope you enjoy my game and have fun. :) <- Savi  


""")


hint = input('If you want a hint enter (y). Otheriwise if your confident enter any value: ')

if hint.lower() == 'y':
    print()
    print("""
The gaurd (%) is a bot thats been programmed to locate the player then move towards him vertically
first. So your best bet is to move horizantly towards the opening at the top of the maze then moving
vertically towards it""")

board = [['-','-','-','-',0,'-','-','-','-','-'],
        [0,0,0,0,0,0,0,0,0,0],
        [0,'|',0,0,'-','-',0,0,'|',0],
        [0,'|',0,0,0,0,0,0,'|',0],
        [0,0,'-','-',0,0,0,0,'|',0],
        [0,0,0,0,0,'-','-',0,0,0],
        ['-','-','-',0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,'-','-','-',0,0,0,'-','-','-'],
        [0,0,0,0,0,0,0,0,0,0]]

agent = '%'
player = '#'
easy = [[9,4],[5,4]]
medium = [[1,0],[7,5]]
hard = [[6,9],[9,9]]
# board[y = vertical axis][x = horizontal axis]
print()
print()
diff = input('Enter the difficulty you want the game to be at (If its your first time I reccomend starting with easy)(e,m,h): ')


if diff.lower() == 'e':
    board[easy[0][0]][easy[0][1]] = agent
    board[easy[1][0]][easy[1][1]] = player
    posA = [easy[0][0],easy[0][1]]
    posP = [easy[1][0],easy[1][1]]
    
    
elif diff.lower() == 'm':
    board[medium[0][0]][medium[0][1]] = agent
    board[medium[1][0]][medium[1][1]] = player
    posA = [medium[0][0],medium[0][1]]
    posP = [medium[1][0],medium[1][1]]
    
    
elif diff.lower() == 'h':
    board[hard[0][0]][hard[0][1]] = agent
    board[hard[1][0]][hard[1][1]] = player
    posA = [hard[0][0],hard[0][1]]
    posP = [hard[1][0],hard[1][1]]
    
    
else:
    print('The value you entered was invalid so we set your difficulty to our default (medium)')
    board[1][0] = agent
    board[7][5] = player
    posA = [1,0]
    posP = [7,5]
    
    
    






grid(board)        
lost = False
won = False

while won != True and lost != True :
    
    posP,board,won = move_player(board,posP,lost)
    lost = check(board,posA,posP,lost)
    board,posA,posP = positions(board,posA,posP,lost)
    
    grid(board)
    if won == True:
        print('YOU WON')
    elif lost == True:
        print('YOU LOST')
    
    
