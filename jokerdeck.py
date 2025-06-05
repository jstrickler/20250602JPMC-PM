from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for n in 1, 2:
            card = Card(f"JOKER{n}", f"JOKER{n}")
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    for _ in range(10):
        print(j.draw())
    print(j)
    print(repr(j))