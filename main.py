import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_cards(deck, num_cards):
    if len(deck) < num_cards:
        raise ValueError("Not enough cards in the deck")
    return deck[:num_cards], deck[num_cards:]

def display_hand(hand):
    return " ".join([f"{rank}{suit[0]}" for rank, suit in hand])

def evaluate_hand(hand, community_cards):
    all_cards = sorted(hand + community_cards, key=lambda x: rank_values[x[0]])
    # ... (Hand evaluation logic remains largely the same, but could be further refined for robustness) ...
    #This section requires significant improvement for a truly robust poker hand evaluator.  Consider using a dedicated poker hand evaluator library for production-level code.

    #Simplified for brevity in this example.  A full implementation would require a much more detailed hand ranking system.
    if all_cards[-1][0] == "A":
        return "High Card", all_cards[-1:]
    else:
        return "High Card", all_cards[-1:]


def get_integer_input(prompt, min_val, max_val):
    while True:
        try:
            num_str = input(prompt)
            num = int(num_str)
            if min_val <= num <= max_val:
                return num
            else:
                raise ValueError(f"Number must be between {min_val} and {max_val}.")
        except ValueError as e:
            print(f"Invalid input: {e}")


def run_poker_simulation():
    while True:
        try:
            num_players = get_integer_input("Enter the number of players (2-10): ", 2, 10)
            num_hands = get_integer_input("Enter the number of hands to deal (1 or more): ", 1, 100)
            hand_size = 2
            num_community_cards = 5
            break
        except ValueError as e:
            print(f"Error: {e}")
            continue

    for hand_num in range(1, num_hands + 1):
        deck = create_deck()
        try:
            community_cards = []
            hands = []
            remaining_deck = deck
            for i in range(num_players):
                hand, remaining_deck = deal_cards(remaining_deck, hand_size)
                hands.append(hand)

            #Deal community cards in stages (Flop, Turn, River)
            flop, remaining_deck = deal_cards(remaining_deck, 3)
            community_cards.extend(flop)
            turn, remaining_deck = deal_cards(remaining_deck, 1)
            community_cards.extend(turn)
            river, remaining_deck = deal_cards(remaining_deck, 1)
            community_cards.extend(river)

            print(f"\n--- Hand {hand_num} ---")
            print("\nCommunity cards:", display_hand(community_cards))
            for i, hand in enumerate(hands):
                hand_rank, high_cards = evaluate_hand(hand, community_cards)
                print(f"Player {i+1}'s hand: {display_hand(hand)} ({hand_rank}, High Cards: {high_cards}")

            #Simplified winning hand determination (needs improvement for real tie-breaking)
            winning_player = 0
            for i in range(1, num_players):
                if rank_values[hands[i][-1][0]] > rank_values[hands[winning_player][-1][0]]:
                    winning_player = i
            print(f"\nPlayer {winning_player + 1} wins!")

        except ValueError as e:
            print(f"Error dealing cards: {e}")
        print("-" * 20)

if __name__ == "__main__":
    run_poker_simulation()
