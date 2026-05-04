from card import Card
import random

class Game:
    def __init__(self, starting_chips=250):
        self.chips = starting_chips
        self.deck = []
        self.current_player_hand = []
        self.second_player_hand = []
        self.dealer_hand = []
        self.is_turn_one = True
        self.current_bet = 0
        self.player_blackjack = False
        self.dealer_blackjack = False
        self.first_hand_total = 0
        
    def __str__(self):
        value = "Chips: "+str(self.chips)+" chips"
        for card in self.deck:
            value = value+"\n  "+str(card)
        return value

    def shuffle_deck(self):
        old_deck = self.deck.copy()
        self.deck.clear()
        copyed_cards = []
        for i in range(len(old_deck)):
            copyed_cards.append(False)
        
        for i in range(len(old_deck)):
            random_card = random.randint(0,len(old_deck)-1)
            while copyed_cards[random_card]:
                random_card = random.randint(0,len(old_deck)-1)
            self.deck.append(old_deck[random_card])

    def fill_deck(self):
        for suit in Card._SUITS:
            for rank in Card._RANKS:
                self.deck.append(Card(rank, suit))

    def draw_card(self):
        if len(self.deck) > 0:
            return self.deck.pop(0)
        return None
    
    def get_card_point_value(self, card):
        try:
            return Card._RANK_VALUES[Card._RANKS.index(card.rank)]
        except:
            return 0
    
    def get_player_point_total(self) -> int:
        total = 0
        ace_total = 0
        for card in self.current_player_hand:
            try:
                total+=self.get_card_point_value(card)
                if card.rank == "A":
                    ace_total+=1
            except:
                pass
        while total > 21 and ace_total > 0:
            total-=10
            ace_total-=1
        return total

    def get_dealer_point_total(self) -> int:
        total = 0
        ace_total = 0
        for card in self.dealer_hand:
            try:
                total+=self.get_card_point_value(card)
                if card.rank == "A":
                    ace_total+=1
            except:
                pass
        while total > 21 and ace_total > 0:
            total-=10
            ace_total-=1
        return total
   
    def start_hand(self):
        self.current_player_hand = []
        self.second_player_hand = []
        self.dealer_hand = []
        self.is_turn_one = True
        self.player_blackjack = False
        self.dealer_blackjack = False

        self.current_player_hand.append(self.draw_card())
        self.dealer_hand.append(self.draw_card())
        self.current_player_hand.append(self.draw_card())
        self.dealer_hand.append(self.draw_card())
        
    def run_dealers_turn(self):
        while self.get_dealer_point_total() < 17:
            self.dealer_hand.append(self.draw_card())

    def get_winner(self):
        if self.get_dealer_point_total() == 21:
            return "dealer"
        if self.get_player_point_total() == 21:
            return "player"
        if self.get_player_point_total() > 21:
            return "dealer"
        if self.get_dealer_point_total() > 21:
            return "player"
        if self.get_dealer_point_total() > self.get_player_point_total():
            return "dealer"
        if self.get_dealer_point_total() < self.get_player_point_total():
            return "player"
        if self.get_dealer_point_total() == self.get_player_point_total():
            return "draw"
        return "error"
        
        
    
'''
if __name__ == "__main__":
    test_game = Game("Jeff")
    test_game.shuffle_deck()
    print(test_game)

    print(Card("jeff"))
'''