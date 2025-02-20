import random
def sum(a, b, c ):
    return a + b + c

def get_move(zState, xState):
    available_moves = [i for i in range(9) if not xState[i] and not zState[i]]
    return random.choice(available_moves) if available_moves else -1
# function to print the board
def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else ' ')
    one = 'X' if xState[1] else ('O' if zState[1] else ' ')
    two = 'X' if xState[2] else ('O' if zState[2] else ' ')
    three = 'X' if xState[3] else ('O' if zState[3] else ' ')
    four = 'X' if xState[4] else ('O' if zState[4] else ' ')
    five = 'X' if xState[5] else ('O' if zState[5] else ' ')
    six = 'X' if xState[6] else ('O' if zState[6] else ' ')
    seven = 'X' if xState[7] else ('O' if zState[7] else ' ')
    eight = 'X' if xState[8] else ('O' if zState[8] else ' ')
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 
# it check wether the win state is reached or not and also prints who won the match and if its a draw it will return -1 from where it was called
def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1

# it stores the initial state of 'X' and 'O'    

xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1 # 1 for X and 0 for O
print("Welcome to Tic Tac Toe")
#it will be true unitl the game gets over or when somebody wins
while(True):
    printBoard(xState, zState)
    if(turn == 1):
        print("X's Chance")
        value = int(input("Please enter a value: "))
        xState[value] = 1
    else:
        print("Computers Chance")
        value = get_move(zState, xState)
        zState[value] = 1
    cwin = checkWin(xState, zState)
    if(cwin != -1):
        print("Match over")
        printBoard(xState,zState)
        break    
    turn = 1 - turn
