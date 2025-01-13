import random

def create_deck():
    SUITS = ['h', 'd', 'c', 's']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [rank + suit for rank in RANKS for suit in SUITS]

def delete_card(cards, deck):
    known_cards = set(cards)
    for card in known_cards:
        if card in deck:
            deck.remove(card)
    return deck

def burn_card(deck):
    if len(deck) > 0:
        burn = random.choice(deck)
        deck.remove(burn)
        return burn
    return None