# 38 field width

hand = list(input())
hand.append('stop')

i = 0
local_i = 0
points = 0
points_total = 0
current_suit = []
suit_names = ['C', 'D', 'H', 'S', 'stop']
suit_names_full = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
points_table = {'A': 4, 'K': 3, 'Q': 2, 'J': 1}

print("Cards Dealt              Points")

while i != len(hand):
    if hand[i] in suit_names:
        if hand[i] == 'C':
            pass

        else:
            if local_i < 3:
                points += 3 - local_i

            print("{0: <30}{1: >}".format(suit_names_full[suit_names.index(hand[i])-1] + " " + ' '.join(current_suit), points))
            local_i = 0
            points_total += points
            points = 0
            current_suit = []

    else:
        current_suit.append(hand[i])
        if hand[i] in points_table:
            points += points_table[hand[i]]

        local_i += 1

    i += 1

print("                       Total {0}".format(points_total))