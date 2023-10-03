cards = input().split()
shuffles = int(input())

for i in range (shuffles):
    middle_of_deck = len(cards) // 2
    left_part = cards[0:middle_of_deck]
    right_part = cards[middle_of_deck:len(cards)+1]
    deck_after_shuffling = []
    for j in range (len(left_part)):
        deck_after_shuffling.append(left_part[j])
        deck_after_shuffling.append(right_part[j])
    cards = deck_after_shuffling

print(cards)
