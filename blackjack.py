
from config import INIT_RDS, WIN, PUSH, SEPARATE_LINE, RepresentsInt
from deck import Decks
from player import Player, Dealer


class Blackjack():
    def __init__(self,num_of_players, num_of_decks):
        #create dealer and players and decks        
        print("----------------------------------------------Game Begins---------------------------------------------\n")    
        self.num_of_players = num_of_players
        self.num_of_decks = num_of_decks
        self.deck = Decks(num_of_decks)
        self.dealer = Dealer(self.deck)
        self.players = [Player(i, self.deck) for i in range(1,num_of_players + 1)]
    
    def set_bet(self):
        for i in range(self.num_of_players):
            print("Player {}\n{}".format(i+1, SEPARATE_LINE))
            while True:
                user_input = input("Please enter the money you bet: ")
                if not RepresentsInt(user_input):
                    print("Please provide an integer input!\n")
                    continue
                
                bet = int(user_input)
                if self.players[i].set_bet(bet):
                    print("\n")
                    break
    
    def initial_rds(self):
        for _ in range(INIT_RDS):
            for i in range(self.num_of_players):
                self.players[i].get_card()
            self.dealer.get_card()

        for player in self.players:   
            player.show_info()
        self.dealer.show_info()
        print("\n")
    

    def players_actions(self):
        print("----------------------------------------------Players' Round---------------------------------------------\n")
        for i in range(self.num_of_players):
            print("\n")
            self.players[i].show_info()
            while True:
                print("\n")
                act = input("Player {} please enter your action for this round(h/sd/d): ".format(i+1))
                print("\n")
                if self.players[i].action(act):
                    self.players[i].show_info()
                    if act == 'sd' or act == 'd':
                        break      


    def dealer_action(self):
        print("----------------------------------------------Dealer's Round---------------------------------------------\n")
        self.dealer.add_cards()   
        self.dealer.show_cards()
        self.dealer.show_info()  
    
    def find_best_sum(self,possible_sum):
        if possible_sum[-1] > 21:
            return possible_sum[-1]
        else:
            for val in possible_sum:
                if val <= 21:
                    return val

    def present_result(self):
        print("----------------------------------------------Results----------------------------------------------------\n")
        possible_dealer_sum = self.dealer.get_card_sum()
        dealer_cards_sum = self.find_best_sum(possible_dealer_sum)
        
        for i in range(self.num_of_players):
            possible_player_sum = self.players[i].get_card_sum()
            player_cards_sum = self.find_best_sum(possible_player_sum)
         
            #lost
            if player_cards_sum > 21 :
                print("Player {} lost!".format(i+1))
            elif player_cards_sum < dealer_cards_sum and dealer_cards_sum <= 21:
                print("Player {} lost!".format(i+1))
            
            #push
            elif player_cards_sum == dealer_cards_sum:
                print("Player {} push!".format(i+1))
                self.players[i].add_money(PUSH)
            #won       
            else:
                print("Player {} won!".format(i+1))
                self.players[i].add_money(WIN)

        print("\n")
        for player in self.players:
            player.show_info()


    def restore(self):
        self.deck.restore_decks()
        self.dealer.restore()
        for player in self.players:
            player.restore()