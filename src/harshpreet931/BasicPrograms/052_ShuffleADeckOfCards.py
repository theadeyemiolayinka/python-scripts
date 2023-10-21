import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

deck = [(rank, suit) for suit in suits for rank in ranks]
random.shuffle(deck)

print("Shuffled Deck:")
for card in deck:
    print(f"{card[0]} of {card[1]}")
