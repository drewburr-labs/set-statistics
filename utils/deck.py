import itertools
from typing import Set

from .card import Card

class Deck ():
    def __init__ (self):
        self.__deck = self.__generateDeck();

    def draw(self, count: int = 1):
        """
        Draw `count` cards from the top of the deck
        """
        cards = [];
        for _ in range(count):
            cards.append(self.deck.pop())
        return cards

    def __generateDeck(self) -> list[Card]:
        """
        Generate a new deck of cards
        """
        cards: list[Card] = []

        for a in range(3):
            for b in range(3):
                for c in range(3):
                    for d in range(3):
                        cards.append(Card(a,b,c,d))

        iterAttributes(attrs: set):
            # if attrs
            # for x in range()



    

    def shuffle(self):
        """
        Shuffle the deck in its current state. 
        """
        pass

    def reset(self):
        pass

    def __sizeof__(self) -> int:
        return len(self.__deck)




