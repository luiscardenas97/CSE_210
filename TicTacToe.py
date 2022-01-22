'''
Solo 01 Prove: Developer - Solo Code Submission
Author: Luis Cardenas
'''
import sys
from termcolor import colored
#To install the module termcolor 'pip install termcolor'
#To install colored 'pip install colored'

def main():
    ''' Holds the main game loop logic
        Selects a player
        Builds the board
        Loops through Players until a winner is found or game is over
        Displays results to user
        Thanks them for playing
        return: None
    '''

        
    board = create_board()
    display_board(board)
    draw = False
    winner = False
    turn = 1
    while draw != True and winner != True:
        # loop if there isn't a winner or if the game isn't a draw​
        # display the board
        # allow the player to make a move​
        # pick the next player
        # display the final board

        # assign/get the first player
        player = next_player(turn)

        make_move(player, board)

        # create a board
        display_board(board)

        draw = is_draw(board)

        winner = is_winner(board)

        turn += 1
    
    # show message that there was a draw
    if draw == True:
        print(colored("You both did your best. This is a draw! ", 'green', attrs = ['bold']))
    
    # show message for winner
    if winner == True:
        if player == "o":
            print(colored("Congratulations player with o's! You have won the game! ", 'blue', attrs = ['bold']))
            
        else:
            print(colored("Congratulations player with x's! You have won the game! ", 'red', attrs = ['bold']))
        
    # show message thanks for playing
    print(colored("\nThank you for playing. \n", 'green', attrs = ['bold']))
    

def create_board():
    ''' Creates a list that holds the spots on the board
        It initializes the positions with the numbers for the person to pick
        return: the board as a list
    '''
    list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9,]]

    return list_1

def display_board(board):
    ''' Displays the current board
        return: None
    '''

    print()
    x = 0
    for _ in board:
        pos_1 = _[0]
        pos_2 = _[1]
        pos_3 = _[2]

        if pos_1 == "x":
            pos_1 = colored(pos_1, 'red', attrs = ['bold'])
        if pos_1 == "o": 
            pos_1 = colored(pos_1, 'blue', attrs = ['bold'])

        if pos_2 == "x":
            pos_2 = colored(pos_2, 'red', attrs = ['bold'])
        if pos_2 == "o":
            pos_2 = colored(pos_2, 'blue', attrs = ['bold'])
            
        if pos_3 == "x":
            pos_3 = colored(pos_3, 'red', attrs = ['bold'])
        if pos_3 == "o":
            pos_3 = colored(pos_3, 'blue', attrs = ['bold'])



        
        print(f"{pos_1} | {pos_2} | {pos_3}")
        x += 1
        if x <= 2:
            print("----------")
    
    print()

    return

def is_draw(board):
    ''' return: True if board is a draw, False if board is still playable '''
    if (board[0][0] == "x" or board[0][0] == "o") and (board[0][1] == "x" or board[0][1] == "o") and (board[0][2] == "x" or board[0][2] == "o") and (board[1][0] == "x" or board[1][0] == "o") and (board[1][1] == "x" or board[1][1] == "o") and (board[1][2] == "x" or board[1][2] == "o") and (board[2][0] == "x" or board[2][0] == "o") and (board[2][1] == "x" or board[2][1] == "o") and (board[2][2] == "x" or board[2][2] == "o") and (board[2][2] == "x" or board[2][2] == "o"):
        draw = True

    else: 
        draw = False
    
    return draw

def is_winner(board):
    ''' return: True if someone won, False if there is no winner '''
    if (board[0][0] == "x" and board[0][1] == "x" and board[0][2] == "x") or (board[0][0] == "o" and board[0][1] == "o"  and board[0][2] == "o"):
        winner = True

    elif (board[1][0] == "x" and board[1][1] == "x" and board[1][2] == "x") or (board[1][0] == "o" and board[1][1] == "o"  and board[1][2] == "o"):
        winner = True

    elif (board[2][0] == "x" and board[2][1] == "x" and board[2][2] == "x") or (board[2][0] == "o" and board[2][1] == "o"  and board[2][2] == "o"):
        winner = True

    elif (board[0][0] == "x" and board[1][0] == "x" and board[2][0] == "x") or (board[0][0] == "o" and board[1][0] == "o"  and board[2][0] == "o"):
        winner = True

    elif (board[0][1] == "x" and board[1][1] == "x" and board[2][1] == "x") or (board[0][1] == "o" and board[1][1] == "o"  and board[2][1] == "o"):
        winner = True

    elif (board[0][2] == "x" and board[1][2] == "x" and board[2][2] == "x") or (board[0][2] == "o" and board[1][2] == "o"  and board[2][2] == "o"):
        winner = True

    elif (board[0][0] == "x" and board[1][1] == "x" and board[2][2] == "x") or (board[0][0] == "o" and board[1][1] == "o"  and board[2][2] == "o"):
        winner = True

    elif (board[0][2] == "x" and board[1][1] == "x" and board[2][0] == "x") or (board[0][2] == "o" and board[1][1] == "o"  and board[2][0] == "o"):
        winner = True

    else:
        winner = False
        
    return winner

def make_move(player, board):
    ''' Prompts player to select a square to play
        Assigns the player to that board location if it is a legal move
        return: None
    '''

    if player == "x":
        turn = 0
        while turn <1 or turn > 9:
            try:
                turn = int(input(f"{player}'s turn to choose a square (1-9): "))
                
                if turn < 1 or turn > 9:
                    print("\nThat's an invalid value. Please try again.\n")

            except ValueError:
                print("\nThat's an invalid character. Please try again.\n")
            except TypeError:
                print("\nThat's an invalid character. Please try again.\n")

    elif player == "o":
        turn = 0
        while turn <1 or turn > 9:
            try:
                turn = int(input(f"{player}'s turn to choose a square (1-9): "))
            
                if turn < 1 or turn > 9:
                    print("\nThat's an invalid value. Please try again.\n")

            except ValueError:
                print("\nThat's an invalid character. Please try again.\n")
            except TypeError:
                print("\nThat's an invalid character. Please try again.\n")

    
    if turn == 1:
        if board[0][0] == "x" or board[0][0] == "o":
            print("\nYou can't use this square. Someone else already chose it. Try again.")   
        else:
            board[0][0] = player

    elif turn == 2:
        if board[0][1] == "x" or board[0][1] == "o":
            print("\nYou can't use this square. Someone else already chose it. Try again.")    
        else: 
            board[0][1] = player

    elif turn == 3:
        if board[0][2] == "x" or board[0][2] == "o":
            print("\nYou can't use this square. Someone else already chose it. Try again.")  
        else:
            board[0][2] = player

    elif turn == 4:
        if board[1][0] == "x" or board[1][0] == "o":
            print("\nYou can't use this square. Someone else already chose it. Try again.")    
        else:
            board[1][0] = player

    elif turn == 5:
        if board[1][1] == "x" or board[1][1] == "o":
            print("\nYou can't use this square. Someone else already chose it. Try again.")    
        else:
            board[1][1] = player

    elif turn == 6:
        if board[1][2] == "x" or board[1][2] == "o":
            print("\nYou can't use this square. Someone else already chose it. Try again.")    
        else:
            board[1][2] = player

    elif turn == 7:
        if board[2][0] == "x" or board[2][0] == "o":
            print("\nYou can't use this square. Someone else already chose it. Try again.")    
        else:
            board[2][0] = player

    elif turn == 8:
        if board[2][1] == "x" or board[2][1] == "o":
            print("\nYou can't use this square. Someone else already chose it. Try again.")    
        else:
            board[2][1] = player

    elif turn == 9:
        if board[2][2] == "x" or board[2][2] == "o":
            print("\nYou can't use this square. Someone else already chose it. Try again.")    
        else:
            board[2][2] = player

    else:
        print("\nThat's an invalid value. Please try again.") 

    return     

def next_player(current):
    ''' return: x if current is o, otherwise x '''

    if (current % 2) == 0:
        player = "o"

    else:
        player = "x"
 
    return player

# run main if this has been called from the command line
if __name__ == "__main__":
    main()