from card import Card
import random

class Game:
    def __init__(self, starting_chips=250):
        self.chips = starting_chips
        self.deck = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.deck.append(Card(rank, suit))

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
        

#if __name__ == "__main__":
#    test_game = Game()