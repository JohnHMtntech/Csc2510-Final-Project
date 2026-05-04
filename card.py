class Card:
    _FILE_SUITS = ["spades", "clubs", "hearts", "diamonds"]
    _FILE_RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
    _RANK_VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    _SUITS = ["S", "C", "H", "D"]
    _RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __new__(cls, rank, suit):
        try:
            Card._RANKS.index(rank)
            Card._SUITS.index(suit)
        except:
            return None
        return super(Card, cls).__new__(cls)
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.texture = Card._FILE_RANKS[Card._RANKS.index(self.rank)]+"_of_"+Card._FILE_SUITS[Card._SUITS.index(self.suit)]+".png"

    def __str__(self):
        return f"Suit: {self.suit} Rank: {self.rank}"