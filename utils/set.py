from .card import Card


class Set():
    def __init__(self, cards: "list[Card]"):
        if len(cards) != 3:
            raise ValueError(
                f"A Set must have exactly 3 cards. Got {len(cards)}")
        self.__cards = cards

    @property
    def isSet(self) -> bool:
        for setValue in sum(self.__cards):
            if setValue % 3 != 0:
                return False

        return True

        # for a, b, c in zip(self.__cards):
        #     if (a+b+c) % 3 != 0:
        #         return False

        # return True
