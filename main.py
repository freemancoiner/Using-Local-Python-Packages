import random


GAME_OPTIONS = {'R': "ROCK", 'S': "SCISSORS", 'P': "Paper"}     # this defines the choices available in the game
GAME_RESULTS = {    # this defines what happens by combining the player and computer choice
    'PR': "covers",
    'SP': "cuts",
}

h = "#################################################################"    
print(f"""{h}
{'Welcome to ROCK-PAPER-SCISSORS'.center(len(h))}
{h}""")

while True:     # starting the game loop
    player = input("\n\tR - ROCK\n\tP - PAPER\n\tS - SCISSORS\nMake your play: ").upper()   # player makes his/her play
    computer = random.choice(list(GAME_OPTIONS.keys()))     # the computer makes its play.

    if not GAME_OPTIONS.get(player):
        print("[-] Invalid Option. Please Try Again!")
        continue

    
    if player == computer:  # asks the player to try again if it is a tie
        print("\nIt is a TIE. Play Again.")
        continue
    else:
        determinant = player + computer     

        if GAME_RESULTS.get(determinant):   
            print("\n\tYou WON!!!")
        else:  
            determinant = determinant[::-1]     
            print("\n\tYou LOSE!!!")

        print(f"\n\t{GAME_OPTIONS.get(determinant[0])} {GAME_RESULTS.get(determinant)} {GAME_OPTIONS.get(determinant[1])}")    
        break