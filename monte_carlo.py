from deck_ import *
import random
from combination import *
from compare_combination import *

def m_carlo(card1, card2, players_count, game_round, community_cards, deck):
                
    players = {i: [] for i in range(players_count)}
    for _ in range(2):
        for i in range(players_count):
            if len(deck) > 0:
                card = random.choice(deck)
                players[i].append(card)
                deck = delete_card(card, deck)
    
    stages = {0: 5, 1: 2, 2: 1, 3: 0}
    pub_cards_to_draw = stages[game_round]
    
    if (pub_cards_to_draw == 5):
        burn_card(deck)
        for i in range(pub_cards_to_draw):
            if (i >= 3):
                burn_card(deck)
            if len(deck) > 0:
                card = random.choice(deck)
                community_cards.append(card)
                deck = delete_card(card, deck)
                
    elif (pub_cards_to_draw == 1 or pub_cards_to_draw == 2):
        for i in range(pub_cards_to_draw):
            burn_card(deck)
            if len(deck) > 0:
                card = random.choice(deck)
                community_cards.append(card)
                deck.remove(card)
    
    # print(f"the public cards: {community_cards}")
    # players_card = players[0]
    # players_card2 = players[1]
    # print(f"players_card: {players_card}")
    # print(f"my cards: {card1, card2}")
    # print(f"best combination player1: {best_combinations(players_card + community_cards)}")
    card1_list = [card1]
    card2_list = [card2]
    # print(f"my best combination: {best_combinations(card1_list + card2_list + community_cards)}")
    # print(f"win: {compare_hands(best_combinations(players_card + community_cards), best_combinations(card1_list + card2_list + community_cards) )}")
    best_others_comb = []
    for i in players:
        best_others_comb.append(best_combinations(players[i] + community_cards))
    # print(f"his best: {best_others_comb}")
    # print(f"my best: {best_combinations(card1_list + card2_list + community_cards)}")
    return compare_multiple_hands(best_combinations(card1_list + card2_list + community_cards), best_others_comb)
    
    