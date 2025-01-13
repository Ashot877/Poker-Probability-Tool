from itertools import combinations
from collections import Counter
from compare_combination import *

def best_combinations(cards):

    combo_list = []
    stop = 0
    
    for combo in combinations(cards, 5):
        
        if (stop <= 10):
            if is_royal_flush(combo):
                combo_list.append(f"10 : {combo}")
                stop = 10
                continue
                
        if (stop <= 9):
            if is_straight_flush(combo):
                combo_list.append(f"9 : {combo}")
                stop = 9
                continue
                
        if (stop <= 8):
            if is_care(combo):
                combo_list.append(f"8 : {combo}")
                stop = 8
                continue
        
        if (stop <= 7):
            if is_full_house(combo):
                combo_list.append(f"7 : {combo}")
                stop = 7
                continue
        
        if (stop <= 6):
            if is_flush(combo):
                combo_list.append(f"6 : {combo}")
                stop = 6
                continue
        
        if (stop <= 5):
            if is_straight(combo):
                combo_list.append(f"5 : {combo}")
                stop = 5
                continue
        
        if (stop <= 4):
            if is_set(combo):
                combo_list.append(f"4 : {combo}")
                stop = 4
                continue
        
        if (stop <= 3):
            if is_two_pair(combo):
                combo_list.append(f"3 : {combo}")
                stop = 3
                continue
        
        if (stop <= 2):
            if is_pair(combo):
                combo_list.append(f"2 : {combo}")
                stop = 2
                continue
    
    if not combo_list:
        card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
    '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
                        }
        
        def card_value(card):
            return card_values[card[:-1]]

        sorted_cards = sorted(cards, key=card_value, reverse=True)
        combo_list.append(f"1 : {sorted_cards[:5]}")
        
    parsed_data = [(int(item.split(' : ')[0]), item.split(' : ')[1]) for item in combo_list]
    try:
        max_key = max(parsed_data, key=lambda x: x[0])[0]
    except Exception as e:
        print(f"errorr : {cards}")
    b_combinations = [item for item in parsed_data if item[0] == max_key]
    
    result = b_combinations[0]
    
    for hand in b_combinations[1:]:
        result = compare_hands(result, hand)

    return result


def is_royal_flush(hand):
    
    suits = [card[-1] for card in hand]
    if len(set(suits)) != 1:
        return False
    
    ranks = [card[:-1] for card in hand]
    royal_flush_values = {'10', 'J', 'Q', 'K', 'A'}
    return set(ranks) == royal_flush_values


def is_straight_flush(hand):
    
    suits = [card[-1] for card in hand]
    ranks = [card[:-1] for card in hand]

    if len(set(suits)) != 1:
        return False
    
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    numeric_ranks = [rank_values[rank] for rank in ranks]
    numeric_ranks.sort()
    
    if numeric_ranks == [2, 3, 4, 5, 14]:
        numeric_ranks = [1, 2, 3, 4, 5]
    
    return numeric_ranks == list(range(numeric_ranks[0], numeric_ranks[0] + 5))


def is_care(hand):
    
    ranks = [card[:-1] for card in hand]
    rank_counts = Counter(ranks)

    return 4 in rank_counts.values()


def is_full_house(hand):

    ranks = [card[:-1] for card in hand]
    rank_counts = Counter(ranks)
    
    return sorted(rank_counts.values()) == [2, 3]


def is_flush(hand):
    
    suits = [card[-1] for card in hand]
    return len(set(suits)) == 1


def is_straight(hand):
    
    ranks = [card[:-1] for card in hand]
    
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    numeric_ranks = [rank_values[rank] for rank in ranks]
    numeric_ranks.sort()
    
    return numeric_ranks == list(range(numeric_ranks[0], numeric_ranks[0] + 5))


def is_set(hand):

    ranks = [card[:-1] for card in hand]
    rank_counts = Counter(ranks)
    return 3 in rank_counts.values()


def is_two_pair(hand):

    ranks = [card[:-1] for card in hand]
    rank_counts = Counter(ranks)
    
    return sorted(rank_counts.values()) == [1, 2, 2]


def is_pair(hand):

    ranks = [card[:-1] for card in hand]
    rank_counts = Counter(ranks)
    
    return 2 in rank_counts.values()