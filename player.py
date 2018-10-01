from config import cards_val, WIN, PUSH, SEPARATE_LINE

class Player():
    def __init__(self, pid, decks):
        self.pid = pid
        self.total_sum = [0]
        self.decks = decks
        self.cards_at_hand = []
        self.money = 2500
        self.cur_bet = 0

    def set_bet(self,bet):
        if bet < 0 or bet > 300:
            print("The bet must be within 0 and 300!\n")
            return False
        if bet > self.money:
            print("Your bet exceeds current money you have!\n")
            return False

        self.cur_bet = bet
        self.money -= bet
        return True

    def get_card(self):
        #get a card
        cur_card = self.decks.random_choose_card()
        self.cards_at_hand.append(cur_card)
        #calculate total sum and act according to the sum
        self.total_sum[0] += cards_val[cur_card]
        if 'A' in self.cards_at_hand:
            #find all possible sums
            num_of_A = self.cards_at_hand.count('A')
            ori_sum = self.total_sum[0]
            self.total_sum = [ori_sum - i * 10 for i in range(num_of_A + 1)]
            
        
            


    def action(self,act):
        if act == 'd':
            #can only double down with initial two cards
            if len(self.cards_at_hand) > 2:
                print("Cannot double down after hit!")
                return False

            if self.money > self.cur_bet:
                self.money -= self.cur_bet
                self.cur_bet *= 2
                self.get_card()
                return True
            else:
                print("Cannot double down, money is not enough!")
                return False
        
        elif act == 'sd':
            return True

        elif act == 'h':
            if all(cards_sum  > 21 for cards_sum in self.total_sum):
                print("Your cards at hand already exceed 21!\n")
                return False
            
            self.get_card()
            return True

        else:
            print("Cannot recognize the action!")
            return False

    def get_card_sum(self):
        return self.total_sum
    
    def add_money(self, status):
        if status == WIN:
            self.money += self.cur_bet * 2
        if status == PUSH:
            self.money += self.cur_bet

    def show_info(self):
        #if he/she is a player
        if self.pid > 0:
            print("Player {}\n{}".format(self.pid,SEPARATE_LINE))
            print("current money: {}".format(self.money),end="    ")
            print("current bet: {}".format(self.cur_bet),end="    ")

        print("current cards at hands: ",end = "",flush = True)
        print(*self.cards_at_hand,end="    ")
        print("sum of cards value: ",end="")
        if self.total_sum[-1] > 21:
            print("{}\n".format(self.total_sum[-1]))
        else:
            for val in self.total_sum:
                if val <= 21:
                    print(val,end=" ")
            print("\n")
        
    
    def restore(self):
        self.cards_at_hand = []
        self.total_sum = [0]
        self.cur_bet = 0

class Dealer(Player):
    def __init__(self,decks):
        super().__init__(0,decks)
        self.reveal_cards = False
    def add_cards(self):
        while self.total_sum[0] < 17:
            self.get_card()
    
    def show_cards(self):
        self.reveal_cards = True
    
    def show_info(self):
        print("Dealer\n{}".format(SEPARATE_LINE))
        if not self.reveal_cards:
            print("current cards at hands: {}, _".format(self.cards_at_hand[0]),end="    ")
            print("sum of cards value: {} + _\n".format(cards_val[self.cards_at_hand[0]]))
        else:
            super().show_info()
