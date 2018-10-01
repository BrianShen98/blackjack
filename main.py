from blackjack import Blackjack
from config import RepresentsInt

def main():
    
    #specify the number of players and number of decks of cards used to play
    while True:
        user_input = input("The number of players to play blackjack: ")
        if not RepresentsInt(user_input):
            print("Please provide an integer input!\n")
            continue
        num_of_players = int(user_input)      
        if num_of_players > 0:
            break

    while True:  
        user_input = input("The number of decks of cards you want to play with: ")
        if not RepresentsInt(user_input):
            print("Please provide an integer input!\n")
            continue
        num_of_decks = int(user_input)
        if num_of_decks > 0:
            break
    print("\n")
    
    #initialize the game
    game = Blackjack(num_of_players,num_of_decks)
   
    while True: 
        #set bet
        game.set_bet() 

        #initial rounds
        game.initial_rds()

        #players take actions
        game.players_actions()

        #dealer's round
        game.dealer_action()

        #compare the result
        game.present_result()

        #ask for another round
        while True:
            ans = input("Another round?(y/n): ")
            if ans == 'n' or ans == 'y':
                break
            else:
                print("Please type y or n!\n")
                
        if ans == 'n':
            break    
        
        #restore the decks of cards if playing another round
        game.restore()
        print("\n")


if __name__ == "__main__":
    main()