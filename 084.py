"""
PROBLEM:     084
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    The indices of the three most likely squares to land on when using two
    four-sided dice in Monopoly, where everyone has infinite money.
"""

from collections import deque, Counter
import types
import numpy as np
import timeit

board = [
    'GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
    'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
    'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
    'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2'
]
railway = [index for index, key in enumerate(board) if key.startswith('R')]
utility = [index for index, key in enumerate(board) if key.startswith('U')]
JAIL = 10

cc = ['GO', 'JAIL'] + [None] * 14
ch = [
    'GO', 'JAIL', 'C1', 'E3', 'H2', 'R1',
    lambda pos: min(railway, key=lambda index: abs(index - pos)),
    lambda pos: min(railway, key=lambda index: abs(index - pos)),
    lambda pos: min(utility, key=lambda index: abs(index - pos)),
    lambda pos: (pos - 3) % len(board)
] + [None] * 6

def get_card(deck, pos):
    card = deck.popleft()
    deck.append(card)
    if card is None:
        return pos

    if isinstance(card, types.FunctionType):
        return card(pos)

    return board.index(card)

def problem():
    # Monte Carlo simulations. Just play the game.
    # We add up the counts from the simulations as it avoids bias from one
    # simulation against the others - a majority operator could also work.
    simulations = 100
    turns = 10000
    eyes = 4
    ndice = 2
    top = 3
    counts = [0] * len(board)
    for sim in range(simulations):
        pos = 0
        same = 0
        np.random.shuffle(cc)
        cc_deck = deque(cc, maxlen=len(cc))
        np.random.shuffle(ch)
        ch_deck = deque(ch, maxlen=len(ch))

        tosses = np.random.choice(np.arange(1, eyes + 1), ndice * turns)
        for turn in range(turns):
            if all(tosses[turn*ndice+1:(turn+1)*ndice] == tosses[turn*ndice]):
                same += 1
                if same == 3:
                    pos = JAIL
                    continue
            else:
                same = 0

            toss = int(sum(tosses[turn*ndice:(turn+1)*ndice]))
            pos = (pos + toss) % len(board)
            if board[pos] == 'G2J':
                pos = JAIL
            if board[pos].startswith('CC'):
                pos = get_card(cc_deck, pos)
            elif board[pos].startswith('CH'):
                pos = get_card(ch_deck, pos)

            counts[pos] += 1

        best = sorted(zip(board, counts), key=lambda p: p[1], reverse=True)

    modal = 0
    for square, count in best[:top]:
        modal = modal * 100 + board.index(square)

    print(modal)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

