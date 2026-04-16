class Card:
    suits = ["S", "C", "H", "D"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, rank, suit="S"):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "Rank: " + self.rank + " Suit: " + self.suit