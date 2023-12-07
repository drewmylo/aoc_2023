import functools
from enum import Enum

class Hand(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

f = open("input.txt", "r")
lines = [line.split(' ') for line in f.read().splitlines()]

card_to_rank_alpha = {
    'J': 'A',
    '2': 'B',
    '3': 'C',
    '4': 'D',
    '5': 'E',
    '6': 'F',
    '7': 'G',
    '8': 'H',
    '9': 'I',
    'T': 'K',
    'Q': 'L',
    'K': 'M',
    'A': 'N'
}

def translate_hand_to_alpha(hand):
    return ''.join([card_to_rank_alpha.get(char) for char in hand])

def get_rank(hand):
    unique_cards = set([char for char in hand])
    unique_cards = unique_cards.difference(set('J'))
    if len(unique_cards) <= 1:
        return Hand.FIVE_OF_A_KIND
    if len(unique_cards) == 2:
        return Hand.FOUR_OF_A_KIND if any((hand.count(element) + hand.count('J')) == 4 for element in unique_cards if 'J' not in element) else Hand.FULL_HOUSE
    if len(unique_cards) == 3:
        return Hand.THREE_OF_A_KIND if any((hand.count(element) + hand.count('J')) == 3 for element in unique_cards if 'J' not in element) else Hand.TWO_PAIR
    if len(unique_cards) == 4:
        return Hand.ONE_PAIR
    return Hand.HIGH_CARD

hands_grouped_by_ranks = {}

sorted_lines = sorted(lines, key = lambda x: (get_rank(x[0]).value, translate_hand_to_alpha(x[0])))
result = 0
for i in range(1, (len(sorted_lines) + 1)):
    result += (int(sorted_lines[i - 1][1]) * i)

print(result)