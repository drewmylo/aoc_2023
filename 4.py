import functools
import queue

total_number_of_cards_touched = 0

card_map = {}

def process_cards(line):
    card_id, numbers = line.split(':')
    winning_numbers, my_numbers = numbers.split('|')
    card_map[get_number_from_card(card_id)] = (my_numbers.split(), set(winning_numbers.split()))

def get_number_from_card(card_id):
    return int(card_id.split()[1])

@functools.lru_cache(120)
def get_total_points(card_id):
    card_id_number = get_number_from_card(card_id)
    card = card_map[card_id_number]
    winnings = 0
    for number in card[0]:
        if number in card[1]:
            winnings += 1
    for x in range(card_id_number + 1, card_id_number + winnings + 1):
        winnings += get_total_points('Card ' + str(x))
    return winnings



f = open("input.txt", "r")

lines = [line for line in f.read().splitlines()]

for line in lines:
    process_cards(line)

for line in lines:
    total_number_of_cards_touched += get_total_points(line.split(':')[0])

print(total_number_of_cards_touched + len(lines))
