from .card import Card
from copy import copy


class Deck ():
    def __init__(self):
        self.__attributes = (3, 3, 3, 3)
        self.__deck = self.__generateDeck()

    @property
    def cards(self) -> "list[Card]":
        """
        Returns a copy of the deck
        """
        newDeck: "list[Card]" = []
        for card in self.__deck:
            newDeck.append(copy(card))

        print(f"new deck length: {len(newDeck)}")
        return newDeck

    def draw(self, count: int = 1):
        """
        Draw `count` cards from the top of the deck
        """
        cards = []
        for _ in range(count):
            cards.append(self.deck.pop())
        return cards

    def __generateDeck(self) -> "list[Card]":
        """
        Generate a new deck of cards
        """
        cards: list[Card] = []

        def generateCardValues(attrs: "set[int]") -> "list[list[int]]":
            """
            The length of attrs describes the number of attributes applied to a card
            The value of each element of attrs describes the number of possible values for that attribute
            For example, a normal deck of playing cards (A-K) would look like (4,13). 4 describes the number of suits,
            while 13 describes the number of cards in that suit. The resulting list will contain 4*13 lists, each with 2 elements.
            This generator will only generate unique cards, with all cards having the same number of attributes.
            """
            card_values: "list[list[int]]" = []
            for x in range(1, attrs[0]+1):
                # Continue if more available
                if attrs[1:]:
                    sub_card_values = generateCardValues(attrs[1:])
                    for card_value in sub_card_values:
                        card_value.append(x)
                    card_values += sub_card_values
                else:
                    card_values.append([x])
            return card_values

        for card_value in generateCardValues(self.__attributes):
            cards.append(Card(card_value))

        return cards

    def shuffle(self):
        """
        Shuffle the deck in its current state.
        """
        pass

    def reset(self):
        pass

    def __sizeof__(self) -> int:
        return len(self.__deck)
