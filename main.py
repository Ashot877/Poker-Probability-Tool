from combination import best_combinations
from monte_carlo import *
from deck_ import *

def main():
    
    deck = create_deck()
    
    while(True):
        players_count = int(input("How many players are in the game without you: "))
        if (1 <= players_count <= 10):
            break
        print("players count must be in [1, 10]\n")
        
    while(True):
        game_round = int(input("Which round: "))
        if (0 <= game_round <= 3):
            break
        print("game round must be in [0, 3]\n")
        
    while(True):
        first_card = input("What is the your first card (example - 3h): ")
        if (first_card in deck):
            deck = delete_card(first_card, deck)
            break
        print("wrong first card\n")
        
    while(True):
        second_card = input("What is the your second card: ")
        if (second_card in create_deck() and second_card != first_card):
            deck = delete_card(second_card, deck)
            break
        print("wrong second card\n")
    
    community_cards = []
    
    if (game_round >= 1):
        while(True):
            pub_firts_card = input("What is the public first card (example - 3h): ")
            if (pub_firts_card in deck):
                deck = delete_card(pub_firts_card, deck)
                community_cards.append(pub_firts_card)
                break
            print("wrong first public card\n")
        while(True):
            pub_second_card = input("What is the public second card: ")
            if (pub_second_card in create_deck()):
                deck = delete_card(pub_second_card, deck)
                community_cards.append(pub_second_card)
                break
            print("wrong second public card\n")
        while(True):
            pub_third_card = input("What is the public third card: ")
            if (pub_third_card in create_deck()):
                deck = delete_card(pub_third_card, deck)
                community_cards.append(pub_third_card)
                break
            print("wrong third public card\n")
        if (game_round >= 2):
            while(True):
                pub_fourth_card = input("What is the public fourth card: ")
                if (pub_fourth_card in create_deck()):
                    deck = delete_card(pub_fourth_card, deck)
                    community_cards.append(pub_fourth_card)
                    break
                print("wrong fourth public card\n")
        if (game_round == 3):
            while(True):
                pub_fifth_card = input("What is the public fifth card: ")
                if (pub_fifth_card in create_deck()):
                    deck = delete_card(pub_fifth_card, deck)
                    community_cards.append(pub_fifth_card)
                    break
                print("wrong fifth public card\n")
                
    count = 0
    
    for i in range(50):
        print(i)   
        count += m_carlo(first_card, second_card, players_count, game_round, community_cards, deck)

    print(f"result: {count/50}")

main()