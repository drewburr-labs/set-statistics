from utils.deck import Deck
from utils.set import Set
import itertools


deck = Deck()

cards = deck.cards

# set_cards = []
# set_cards.append(cards.pop())
# set_cards.append(cards.pop())
# set_cards.append(cards.pop())
# print(set_cards)
# testSet = Set(set_cards)
# print(testSet.isSet)

# Get all possible plays from a deck of cards
plays = itertools.combinations(cards, 12)

total_plays = sum(1 for _ in plays)

print(f"Total combinations {total_plays}")
