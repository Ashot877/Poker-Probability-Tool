def parse_cards(cards_str):
    
    values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
        '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }
    
    cards = cards_str.strip("()").replace("'", "").split(", ")
    cards_with_values = []
    for card in cards:
        if '[' in card:
            card = card[1:]
            continue
        if card[:2] == '10':
            value = '10'
        else:
            value = card[0]
        cards_with_values.append((values[value], card))
    
    #sorted_cards = [card for _, card in sorted(cards_with_values, reverse=True, key=lambda x: x[0])]
    sorted_cards = sorted(cards_with_values, reverse=True, key=lambda x: x[0])
    sorted_values = [value for value, _ in sorted_cards]
    return sorted_values
    
def compare_hands(hand1, hand2):
    
    rank1, rank2 = hand1[0], hand2[0]
    if rank1 > rank2:
        return hand1
    elif rank2 > rank1:
        return hand2
    
    cards1 = parse_cards(hand1[1])
    cards2 = parse_cards(hand2[1])
    
    for c1, c2 in zip(cards1, cards2):
        if c1 > c2:
            return hand1
        elif c2 > c1:
            return hand2
    
    return hand1

def compare_multiple_hands(my_hand, others_hands):
    
    for hand in others_hands:
        rank1, rank2 = my_hand[0], hand[0]
        if rank1 > rank2:
            continue
        elif rank2 > rank1:
            print(hand)
            return 0
    
        cards1 = parse_cards(my_hand[1])     
        cards2 = parse_cards(hand[1])
        for c1, c2 in zip(cards1, cards2):
            if c1 > c2:
                continue
            elif c2 > c1:
                print(hand)
                return 0
    
    return 1
