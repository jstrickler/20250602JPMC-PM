import random
from card import Card

class CardDeck:
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self):
        self._make_deck()
    
    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_suits(cls):
        return cls.SUITS
    
    def __str__(self):
        name = type(self).__name__
        return f"{name}:{len(self._cards)}"
    
    def __repr__(self):
        name = type(self).__name__
        return f"{name}()"

# normal code
# another class
# etc etc

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    print(f"{d1.cards = }")
    d1.shuffle()
    for i in range(5):
        card = d1.draw()
        print(card)
    print()
    print(f"{d1.get_suits() = }")
    print(f"{CardDeck.get_suits() = }")
    print(d1)
    print(repr(d1))

    