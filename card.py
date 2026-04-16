class Card:
    _suits = ["spades", "clubs", "hearts", "diamonds"]
    _ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
    suits = ["S", "C", "H", "D"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __new__(cls, rank, suit="S"):
        try:
            Card.ranks.index(rank)
        except:
            return None
        try:
            Card.suits.index(suit)
        except:
            return None
        return super(Card, cls).__new__(cls)
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.texture = Card._ranks[Card.ranks.index(self.rank)]+"_of_"+Card._suits[Card.suits.index(self.suit)]+".png"

    def __str__(self):
        return self.texture