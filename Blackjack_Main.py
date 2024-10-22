import Day11BlackjackArt
import random
import time
import os
import sys

def clear_last_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(seconds):
    time.sleep(seconds)

def card_value(card):
    if 'k' in card or 'q' in card or 'j' in card:
        return 10
    elif 'a' in card:
        return 11
    else:
        try:
            return int(card[1:])
        except ValueError:
            print(f"Invalid card value: {card}")
            return 0

def refresh(player_cards, dealer_cards, balance, done, bet=None, bet1=None, bet2=None, split=False, player_split1=None, player_split2=None):
    clear()
    print(Day11BlackjackArt.logo)
    print(Day11BlackjackArt.lines)
    if split:
        display_split_cards(player_split1, player_split2, dealer_cards, done, bet1, bet2)
    else:
        display_cards(player_cards, dealer_cards, done)
    print(Day11BlackjackArt.lines)
    if not split:
        print(f"\nYour bet: ${bet}")
    print(f"Your current balance is ${balance}\n")

def total(cards):
    total_value = 0
    ace_count = 0
    for card in cards:
        value = card_value(card)
        if value == 11:
            ace_count += 1
        else:
            total_value += value

    while ace_count > 0:
        if total_value + 11 <= 21:
            total_value += 11
        else:
            total_value += 1
        ace_count -= 1
    
    return total_value

def display_cards(player_cards, dealer_cards, done):
    player_art = [Day11BlackjackArt.card_art[card].strip().splitlines() for card in player_cards]
    dealer_art = [Day11BlackjackArt.card_art[card].strip().splitlines() for card in dealer_cards]
    blank_card_art = Day11BlackjackArt.card_art["blank"].strip().splitlines()

    max_lines = max(max(len(card) for card in player_art), max(len(card) for card in dealer_art), len(blank_card_art))

    first_line_spacing = " " * 5
    additional_spacing = " " * 1
    regular_spacing = " " * 5

    print("\nDealer Cards:")
    for i in range(max_lines):
        dealer_line = ""
        if done == 0:
            for n in range(len(dealer_art)):
                if n == 1:
                    card_art = blank_card_art[i] if i < len(blank_card_art) else " " * len(blank_card_art[0])
                else:
                    card_art = dealer_art[n][i] if i < len(dealer_art[n]) else " " * len(dealer_art[n][0])
                
                if i == 0 and n > 0:
                    dealer_line += first_line_spacing + additional_spacing
                
                dealer_line += card_art + regular_spacing
        else:
            for n in range(len(dealer_art)):
                card_art = dealer_art[n][i] if i < len(dealer_art[n]) else " " * len(dealer_art[n][0])
                
                if i == 0 and n > 0:
                    dealer_line += first_line_spacing + additional_spacing
                
                dealer_line += card_art + regular_spacing

        if i == 0:
            dealer_line = first_line_spacing + dealer_line
        print(dealer_line)

    if done:
        print(f"\nTotal = {total(dealer_cards)}")
    else:
        print("\nTotal = ?")

    print("\nPlayer Cards:")
    for i in range(max_lines):
        player_line = ""
        for n in range(len(player_art)):
            card_art = player_art[n][i] if i < len(player_art[n]) else " " * len(player_art[n][0])
            
            if i == 0 and n > 0:
                player_line += first_line_spacing + additional_spacing
            
            player_line += card_art + regular_spacing

        if i == 0:
            player_line = first_line_spacing + player_line
        print(player_line)

    print(f"\nTotal = {total(player_cards)}")

def display_split_cards(split1, split2, dealer_cards, done, bet1, bet2):
    split1_art = [Day11BlackjackArt.card_art[card].strip().splitlines() for card in split1] if split1 else [[" "]]
    split2_art = [Day11BlackjackArt.card_art[card].strip().splitlines() for card in split2] if split2 else [[" "]]
    dealer_art = [Day11BlackjackArt.card_art[card].strip().splitlines() for card in dealer_cards] if dealer_cards else [[" "]]
    blank_card_art = Day11BlackjackArt.card_art["blank"].strip().splitlines()

    max_lines = max(max(len(card) for card in split1_art), max(len(card) for card in split2_art), max(len(card) for card in dealer_art), len(blank_card_art))

    first_line_spacing = " " * 5
    additional_spacing = " " * 1
    regular_spacing = " " * 5

    print("\nDealer Cards:")
    for i in range(max_lines):
        dealer_line = ""
        if done == 0:
            for n in range(len(dealer_art)):
                if n == 1:
                    card_art = blank_card_art[i] if i < len(blank_card_art) else " " * len(blank_card_art[0])
                else:
                    card_art = dealer_art[n][i] if i < len(dealer_art[n]) else " " * len(dealer_art[n][0])
                
                if i == 0 and n > 0:
                    dealer_line += first_line_spacing + additional_spacing
                
                dealer_line += card_art + regular_spacing
        else:
            for n in range(len(dealer_art)):
                card_art = dealer_art[n][i] if i < len(dealer_art[n]) else " " * len(dealer_art[n][0])
                
                if i == 0 and n > 0:
                    dealer_line += first_line_spacing + additional_spacing
                
                dealer_line += card_art + regular_spacing

        if i == 0:
            dealer_line = first_line_spacing + dealer_line
        print(dealer_line)

    if done:
        print(f"\nTotal = {total(dealer_cards)}")
    else:
        print("\nTotal = ?")

    print("\nHand 1:")
    for i in range(max_lines):
        hand1_line = ""
        for n in range(len(split1_art)):
            card_art = split1_art[n][i] if i < len(split1_art[n]) else " " * len(split1_art[n][0])
            
            if i == 0 and n > 0:
                hand1_line += first_line_spacing + additional_spacing
            
            hand1_line += card_art + regular_spacing
        if i == 0:
            hand1_line = first_line_spacing + hand1_line
        print(hand1_line)
    print(f"\nTotal = {total(split1)}")
    print(f"Hand 1 bet: ${bet1}")

    print("\nHand 2:")
    for i in range(max_lines):
        hand2_line = ""
        for n in range(len(split2_art)):
            card_art = split2_art[n][i] if i < len(split2_art[n]) else " " * len(split2_art[n][0])
            
            if i == 0 and n > 0:
                hand2_line += first_line_spacing + additional_spacing
            
            hand2_line += card_art + regular_spacing
        if i == 0:
            hand2_line = first_line_spacing + hand2_line
        print(hand2_line)
    print(f"\nTotal = {total(split2)}")
    print(f"Hand 2 bet: ${bet2}")

def has_soft_17(cards):
    total_value = 0
    ace_count = 0
    for card in cards:
        value = card_value(card)
        if value == 11:
            ace_count += 1
        total_value += value

    return ace_count > 0 and total_value == 17

balance = 60
initial_bet = 10

while balance > 0:
    bet = initial_bet
    deck = [
        "ca", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cj", "cq", "ck",
        "da", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dj", "dq", "dk",
        "ha", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hj", "hq", "hk",
        "sa", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sj", "sq", "sk"
    ]
    player_cards = []
    dealer_cards = []
    player_split1 = []
    player_split2 = []
    split = False
    done = 0
    clear()
    
    while True:
        clear()
        print(Day11BlackjackArt.logo)
        print(Day11BlackjackArt.lines)
        print(Day11BlackjackArt.rules)
        print(Day11BlackjackArt.lines)
        print(f"\nYour bet: ${bet}")
        print(f"Your current balance is ${balance}")
        deal = input("\nHow much would you like to bet? To keep the same bet, type 'd' to deal.\n")

        if deal == 'd':
            if bet <= 0 or bet > balance:
                print("Invalid bet amount. Please enter a valid bet.")
                wait(2)
                clear_last_line()
                clear_last_line()
            else:
                break
        else:
            try:
                new_bet = int(deal)
                if new_bet >= 10 and new_bet <= balance:
                    bet = new_bet  # Update bet
                    initial_bet = bet
                    break
                else:
                    print("Invalid bet amount. Please enter a valid bet.")
                    wait(2)
                    clear_last_line()
                    clear_last_line()
            except ValueError:
                print("Invalid input. Please enter a number or 'd' to deal.")
                wait(2)
                clear_last_line()
                clear_last_line()

    p1 = random.choice(deck)
    player_cards.append(p1)
    deck.remove(p1)
    p2 = random.choice(deck)
    player_cards.append(p2)
    deck.remove(p2)
    d1 = random.choice(deck)
    dealer_cards.append(d1)
    deck.remove(d1)
    d2 = random.choice(deck)
    dealer_cards.append(d2)
    deck.remove(d2)
    
    player_total = total(player_cards)
    dealer_total = total(dealer_cards)
    
    refresh(player_cards, dealer_cards, balance, done, bet)
    
    # Player's turn
    choice = 'h'
    dealer_blackjack = dealer_total == 21
    hits = 0
    if dealer_blackjack:
        choice = 'n'
    while choice != 'n' and player_total <= 21:
        nc = 0
        if player_total == 21:
            choice = 'n'
        elif card_value(player_cards[0]) == card_value(player_cards[1]) and hits == 0:
            move = 0
            choice = input("Type 'h' to take a hit, 'd' to double down, 's' to split, or 'n' to stand.\n")
            repeat = 0
            while move == 0:
                if repeat == 1:
                    choice = input()
                    repeat = 0
                if choice in ['d', 's']:
                    if (bet * 2) > balance:
                        print("Insufficient funds. Please make another selection.")
                        wait(2)
                        clear_last_line()
                        clear_last_line()
                        repeat = 1
                    else:
                        if choice == 'd':
                            bet *= 2
                            move = 1
                            hits += 1
                            nc = 1
                        elif choice == 's':
                            bet1 = bet
                            bet2 = bet
                            move = 1
                            hits += 1
                            nc = 1
                            split = True
                            player_split1 = [player_cards[0]]
                            player_split2 = [player_cards[1]]
                            new_card1 = random.choice(deck)
                            player_split1.append(new_card1)
                            deck.remove(new_card1)
                            new_card2 = random.choice(deck)
                            player_split2.append(new_card2)
                            deck.remove(new_card2)
                            refresh(None, dealer_cards, balance, done, bet1 = bet1, bet2 = bet2, split=True, player_split1=player_split1, player_split2=player_split2)
                            wait(1)
                            choice = 'n'
                            break
                elif choice == 'h':
                    move = 1
                    hits += 1
                    nc = 1
                elif choice == 'n':
                    move = 1
                else:
                    print("Invalid selection. Please try again.")
                    wait(2)
                    clear_last_line()
                    clear_last_line()
        elif hits == 0:
            move = 0
            choice = input("Type 'h' to take a hit, 'd' to double down, or 'n' to stand.\n")
            repeat = 0
            while move == 0:
                if repeat == 1:
                    choice = input()
                    repeat = 0
                if choice in ['d']:
                    if (bet * 2) > balance:
                        print("Insufficient funds. Please make another selection.")
                        wait(2)
                        clear_last_line()
                        clear_last_line()
                        repeat = 1
                    else:
                        if choice == 'd':
                            bet *= 2
                            move = 1
                            hits += 1
                            nc = 1
                elif choice == 'h':
                    move = 1
                    hits += 1
                    nc = 1
                elif choice == 'n':
                    move = 1
                else:
                    print("Invalid selection. Please try again.")
                    wait(2)
                    clear_last_line()
                    clear_last_line()
                    repeat = 1
        else:
            move = 0
            while move == 0:
                choice = input("Type 'h' to take a hit or 'n' to stand.\n")
                if choice == 'h':
                    move = 1
                    hits += 1
                    nc = 1
                elif choice == 'n':
                    move = 1
                else:
                    print("Invalid selection. Please try again.")
                    wait(2)
                    clear_last_line()
                    clear_last_line()
                    repeat = 1
        if nc == 1 and choice in ['h', 'd']:
            new = random.choice(deck)
            player_cards.append(new)
            player_total = total(player_cards)
            refresh(player_cards, dealer_cards, balance, done, bet)
            wait(1)

            if choice == 'd' or player_total == 21:
                choice = 'n'

    if choice == 's':
        split = True
        bet1 = bet
        bet2 = bet1
        player_split1 = [player_cards[0]]
        player_split2 = [player_cards[1]]
        player_cards = []
        new_card1 = random.choice(deck)
        player_split1.append(new_card1)
        deck.remove(new_card1)
        new_card2 = random.choice(deck)
        player_split2.append(new_card2)
        deck.remove(new_card2)
        refresh(None, dealer_cards, balance, done, bet1 = bet1, bet2 = bet2, split=True, player_split1=player_split1, player_split2=player_split2)
        wait(1)

    
    if not split:
        # Dealer's turn
        done = 1
        skip = 0
        refresh(player_cards, dealer_cards, balance, done, bet)
        wait(2)
        if player_total == 21 and hits == 0:
            print("You have Blackjack!!!")
            wait(2)
            skip = 1
            balance += bet * 2
        elif dealer_blackjack:
            print("Dealer has Blackjack!")
            wait(2)
            balance -= bet
            skip = 1
        elif player_total <= 21:
            while dealer_total < 17 or (dealer_total == 17 and has_soft_17(dealer_cards)):
                new = random.choice(deck)
                dealer_cards.append(new)
                deck.remove(new)
                dealer_total = total(dealer_cards)
                refresh(player_cards, dealer_cards, balance, done, bet)
                wait(1)
                
        if player_total > 21:
            print("You busted! You lose.")
            wait(2)
            balance -= bet
        elif dealer_total > 21 or player_total > dealer_total:
            print("You Win!")
            wait(2)
            if skip == 0:
                balance += bet
        elif player_total < dealer_total:
            print("You Lose!")
            wait(2)
            if skip == 0:
                balance -= bet
        else:
            print("It's a Push!")
            wait(2)
    else:
        # Player's turn for split hands
        for i, split_hand in enumerate([player_split1, player_split2]):
            choice = 'h'
            hits = 0
            aces_split = card_value(split_hand[0]) == 11

            while choice != 'n' and total(split_hand) <= 21:
                nc = 0
                move = 0
                while move == 0:
                    if hits == 0:
                        if aces_split:
                            choice = 'n'
                            break
                        else:
                            choice = input(f"Hand {i + 1} (Bet: ${bet1 if i == 0 else bet2}): Type 'h' to take a hit, 'd' to double down, or 'n' to stand.\n")
                            repeat = 0
                            bc = 0
                            while repeat == 0:
                                if bc == 1:
                                    choice = input()
                                if choice in ['d']:
                                    if ((bet1 if i == 0 else bet2) * 2) > balance:
                                        print("Insufficient funds. Please make another selection.")
                                        wait(2)
                                        clear_last_line()
                                        clear_last_line()
                                        bc = 1
                                    else:
                                        if choice == 'd':
                                            repeat = 1
                                            if i == 0:
                                                bet1 *= 2
                                            else:
                                                bet2 *= 2
                                            move = 1
                                            hits += 1
                                            nc = 1
                                elif choice == 'h':
                                    move = 1
                                    hits += 1
                                    nc = 1
                                    repeat = 1
                                elif choice == 'n' or total(split_hand) == 21:
                                    move = 1
                                    choice = 'n'
                                    repeat = 1
                                else:
                                    print("Invalid selection. Please try again.")
                                    wait(2)
                                    clear_last_line()
                                    clear_last_line()
                                    bc = 1
                    else:
                        choice = input(f"Hand {i + 1} (Bet: ${bet1 if i == 0 else bet2}): Type 'h' to take a hit or 'n' to stand.\n")
                        repeat = 0
                        bc = 0
                        while repeat == 0:
                            if bc == 1:
                                choice = input()
                            if choice == 'h':
                                move = 1
                                hits += 1
                                nc = 1
                                repeat = 1
                            elif choice == 'n' or total(split_hand) == 21:
                                move = 1
                                choice = 'n'
                                repeat = 1
                            else:
                                print("Invalid selection. Please try again.")
                                wait(2)
                                clear_last_line()
                                clear_last_line()
                                bc = 1

                if nc == 1 and (choice == 'h' or choice == 'd'):
                    new = random.choice(deck)
                    split_hand.append(new)
                    refresh(None, dealer_cards, balance, done, bet1 = bet1, bet2 = bet2, split=True, player_split1=player_split1, player_split2=player_split2)
                    wait(1)
                    if choice == 'd' or total(split_hand) == 21:
                        choice = 'n'

            if total(split_hand) > 21:
                print(f"Hand {i + 1} busted!")
                if i == 0:
                    balance -= bet1
                else:
                    balance -= bet2
            else:
                print(f"Hand {i + 1} stands at {total(split_hand)}")
            refresh(None, dealer_cards, balance, done, bet1 = bet1, bet2 = bet2, split=True, player_split1=player_split1, player_split2=player_split2)
            wait(1)
        
        # Dealer's turn after split hands
        done = 1
        refresh(None, dealer_cards, balance, done, bet1 = bet1, bet2 = bet2, split=True, player_split1=player_split1, player_split2=player_split2)
        wait(2)
        while dealer_total < 17 or (dealer_total == 17 and has_soft_17(dealer_cards)):
            new = random.choice(deck)
            dealer_cards.append(new)
            deck.remove(new)
            dealer_total = total(dealer_cards)
            refresh(None, dealer_cards, balance, done, bet1 = bet1, bet2 = bet2, split=True, player_split1=player_split1, player_split2=player_split2)
            wait(1)

        for i, split_hand in enumerate([player_split1, player_split2]):
            bet_current = bet1 if i == 0 else bet2
            if total(split_hand) <= 21:
                if dealer_total > 21 or total(split_hand) > dealer_total:
                    print(f"Hand {i + 1} wins!")
                    balance += bet_current
                elif total(split_hand) < dealer_total:
                    print(f"Hand {i + 1} loses!")
                    balance -= bet_current
                else:
                    print(f"Hand {i + 1} pushes!")
            wait(2)

    wait(1)
    if balance < 10:
        print("You ran out of money! Time to hit the ATM!")
        break

print("Thanks for playing!")