def display_board(board):
    print("""
+-------+-------+-------+
|       |       |       |
|  """,game[0][0],"     ",game[0][1],"     ",game[0][2],"""   
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   """,game[1][0],"    ",game[1][1],"      ",game[1][2],"""   
|       |       |       |
+-------+-------+-------+
|       |       |       |
| """,game[2][0],"   |  ",game[2][1],"      ",game[2][2],"""   
|       |       |       |
+-------+-------+-------+
          """)
    print("turn  ",board)

    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

def  enter_move(board):
    num=int(input("enter number between 1 and 9 "))
    if num not in range(1,10):
        print("invalid number ")
        return 0
        
    if not make_list_of_free_fields(num):
        print("already occupied")
        return 0
    else:
        return num
        
# The function accepts the board's current status, asks the user about their move, 
# checks the input, and updates the board according to the user's decision.
def make_list_of_free_fields(board):
    free=[]
    for i in range(len(game)):
        for j in range (len(game[i])):
            if game[i][j] in range(1,10):
                free.append((i,j))
    
    if board==0:
        return len(free)
    else:
        for i in free:
             x,y=i
             if game[x][y]==board:
                 return True
        return False
         
        
          
        
            
# The function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    for i in range(len(game)):
        if game[i][0]==sign and game[i][1]==sign and game[i][2]==sign:
            return 1
        if game[0][i]==sign and game[1][i]==sign and game[2][i]==sign:
            return 1
    if game[0][0]==sign and game[1][1]==sign and game[2][2]==sign:
        return 1
    if game[0][2]==sign and game[1][1]==sign and game[2][0]==sign:
        return 1
    check=make_list_of_free_fields(0)
    if check==0:
        return 2
    else:
        return 3
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    from random import randrange
    num=randrange(1,9)
    while not make_list_of_free_fields(num):
        num=randrange(1,9)
    
    return num
# The function draws the computer's move and updates the board.
    
game=[[1,2,3],[4,"X",6],[7,8,9]]
turn=1
phase=True
while phase:
    display_board(turn)
    move=enter_move(turn)
    
    if move==0:
        continue
    else:
        for i in range(len(game)):
            for j in range(len(game[i])):
                if move==game[i][j]:
                    game[i][j]="O"
                    turn+=1            
    check=victory_for(turn, "O")
    if check==1:
        print("you won ")
        phase=False
        break
    elif check==2:
        print("Tie ")
        phase=False
        break
    elif check==3:
        phase=True
        
    move=draw_move(turn)
    for i in range(len(game)):
            for j in range(len(game[i])):
                if move==game[i][j]:
                    game[i][j]="X"
                    turn+=1        
    
    check=victory_for(turn, "X")
    if check==1:
        print("computer won ")
        phase=False
        break
    elif check==2:
        print("Tie ")
        phase=False
        break
    elif check==3:
        phase=True
    
    
