"""
PROBLEM:     054
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of Poker hands won by Player 1
"""

import timeit

order = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
index = lambda cards: tuple(order.index(card) for card in cards)
def reorder(cards, suit):
    return zip(*sorted(zip(index(cards), suit)))

royal = index(('T', 'J', 'Q', 'K', 'A'))

ranks = (
    # High Card: Highest value card.
    lambda card, suit, patterns: card[-1],
    # One Pair: Two cards of the same value.
    lambda card, suit, patterns: len(patterns['pairs']) >= 1 and patterns['pairs'][0],
    # Two Pairs: Two different pairs.
    lambda card, suit, patterns: len(patterns['pairs']) >= 2 and patterns['pairs'][-1],
    # Three of a Kind: Three cards of the same value.
    lambda card, suit, patterns: patterns['three'],
    # Straight: All cards are consecutive values.
    lambda card, suit, patterns: patterns['consecutive'],
    # Flush: All cards of the same suit.
    lambda card, suit, patterns: patterns['flush'],
    # Full House: Three of a kind and a pair.
    lambda card, suit, patterns: patterns['three'] and any(pair != patterns['three'] for pair in patterns['pairs']),
    # Four of a Kind: Four cards of the same value.
    lambda card, suit, patterns: (
        (len(set(card[:-1])) == 1 and card[3]) or
        (len(set(card[1:])) == 1 and card[4])
    ),
    # Straight Flush: All cards are consecutive values of same suit.
    lambda card, suit, patterns: patterns['flush'] and patterns['consecutive'],
    # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    lambda card, suit, patterns: patterns['flush'] and card == royal
)

def calc(card, suit):
    zipped = zip(card[:-1], card[1:])
    return {
        'consecutive': card[-1] if all(prev == card - 1 for prev, card in zipped) else False,
        'flush': len(set(suit)) == 1 and card[-1],
        'three': (
            (len(set(card[:-2])) == 1 and card[2]) or
            (len(set(card[1:-1])) == 1 and card[3]) or
            (len(set(card[2:])) == 1 and card[4])
        ),
        'pairs': [card for prev, card in zipped if prev == card]
    }

def problem():
    wins = 0
    with open('p054_poker.txt') as poker:
        for line in poker:
            card1, suit1 = reorder(line[0:3*5:3], line[1:3*5:3])
            card2, suit2 = reorder(line[3*5::3], line[3*5+1::3])
            patterns1 = calc(card1, suit1)
            patterns2 = calc(card2, suit2)
            rank1 = len(ranks)
            value1 = False
            while value1 is False:
                rank1 -= 1
                value1 = ranks[rank1](card1, suit1, patterns1)

            rank2 = len(ranks)
            value2 = False
            while value2 is False and rank2 >= rank1:
                rank2 -= 1
                value2 = ranks[rank2](card2, suit2, patterns2)

            wins += rank1 > rank2 or (rank1 == rank2 and value1 > value2) or \
                (rank1 == rank2 and value1 == value2 and reversed(card1) > reversed(card2))

    print(wins)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
