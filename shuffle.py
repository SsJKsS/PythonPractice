# import random as rd
#
# def drawCards():
#     deck = []
#     for i in suit:
#         for j in card:
#             deck.append(i + j)
#
#     rd.shuffle(deck)
#     print(deck.pop())
#     print(deck.pop())
#     print(deck.pop())
#     print(deck.pop())
#     print(deck.pop())
#
#
# suit = ["♠", "♥", "♦", "♣"]
# card = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# drawCards()

import random

deck = set({})
suit = ["♠", "♥", "♦", "♣"]
card = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

while len(deck)!=5:
    deck.add(random.choice(suit)+random.choice(card))

print(deck)




