import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_cards(deck, num_players, hand_size, num_community_cards):
    deck_size = len(deck)
    required_cards = num_players * hand_size + num_community_cards
    if deck_size < required_cards:
        raise ValueError(f"Not enough cards in the deck to deal {num_players} hands. Need {required_cards}, have {deck_size}.")

    community_cards = deck[:num_community_cards]
    player_hands = []
    start_index = num_community_cards
    for i in range(num_players):
        end_index = start_index + hand_size
        player_hands.append(deck[start_index:end_index])
        start_index = end_index
    return community_cards, player_hands


def display_hand(hand):
    return " ".join([f"{rank}{suit[0]}" for rank, suit in hand])

#Improved hand evaluation using a simplified approach.  A full implementation would require a much more complex algorithm.
def evaluate_hand(hand, community_cards):
    all_cards = sorted(hand + community_cards, key=lambda x: rank_values[x[0]])
    
    #Check for flush (simplified - only checks for same suit in the last 5 cards)
    if all(card[1] == all_cards[-1][1] for card in all_cards[-5:]):
        return "Flush"

    #Check for straight (simplified - only checks for consecutive ranks in the last 5 cards)
    if all(rank_values[all_cards[i+1][0]] == rank_values[all_cards[i][0]] + 1 for i in range(len(all_cards)-5, len(all_cards)-1)):
        return "Straight"

    #Check for pairs, three of a kind, four of a kind (simplified)
    rank_counts = {}
    for rank, _ in all_cards:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1

    counts = list(rank_counts.values())
    if 4 in counts:
        return "Four of a Kind"
    if 3 in counts and 2 in counts:
        return "Full House"
    if 3 in counts:
        return "Three of a Kind"
    if counts.count(2) == 2:
        return "Two Pair"
    if 2 in counts:
        return "Pair"
    return "High Card"


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

    for hand_num in range(1, num_hands + 1):
        deck = create_deck()
        try:
            community_cards, hands = deal_cards(deck, num_players, hand_size, num_community_cards)
            print(f"\n--- Hand {hand_num} ---")
            print("\nCommunity cards:", display_hand(community_cards))
            for i, hand in enumerate(hands):
                hand_rank = evaluate_hand(hand, community_cards)
                print(f"Player {i+1}'s hand: {display_hand(hand)} ({hand_rank})")
        except ValueError as e:
            print(f"Error dealing cards: {e}")
        print("-" * 20)


if __name__ == "__main__":
    run_poker_simulation()
