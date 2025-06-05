class Card:  # inherits from 'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
    
    @property  # decorator
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit
    
    def __str__(self):  #  str(Card-obj)
        return f"{self.rank}:{self.suit}"

    def __repr__(self):  # repr(Card-obj)
        return f"Card('{self.rank}', '{self.suit}')"
    
if __name__ == "__main__":
    c1 = Card('8', 'Diamonds')
    c2 = Card('K', "Hearts")
    print(c1)
    print(repr(c1))
    print(f"{c1.rank = }")
    print(f"{c2.suit = }")
    
