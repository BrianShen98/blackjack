from random import choices

class Decks():
    def __init__(self,num_of_decks):
        self.num_of_decks = num_of_decks
        self.num_of_cards = 52 * self.num_of_decks
       
        #the number of cards remaning for each card value
        self.cards_remain = {k : 4 * self.num_of_decks for k in '23456789AJQK'}
        self.cards_remain["10"] = 4 * self.num_of_decks
    
    def random_choose_card(self):
        card = choices(list(self.cards_remain.keys()), list(self.cards_remain.values()))[0]
        self.cards_remain[card] -= 1
        self.num_of_cards -= 1
        if self.cards_remain[card] < 0:
            print("Remaining card cannot be less than 0!\n")
            exit(1)
        
        return card

    def restore_decks(self):
        self.num_of_cards = 52 * self.num_of_decks
        self.cards_remain = {k : 4 * self.num_of_decks for k in '23456789AJQK'}
        self.cards_remain["10"] = 4 * self.num_of_decks
