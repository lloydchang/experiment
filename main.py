import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

def create_deck():
    """Creates and shuffles a standard 52-card deck."""
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_cards(deck, num_players, hand_size, num_community_cards):
    """Deals cards to players and the community."""
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
    """Displays a hand in a user-friendly format."""
    return " ".join([f"{rank}{suit[0]}" for rank, suit in hand])

#Improved Hand Evaluation (Still simplified, but better than before)
def evaluate_hand(hand, community_cards):
    all_cards = sorted(hand + community_cards, key=lambda x: rank_values[x[0]])
    
    #Check for Flush
    suits = {}
    for card in all_cards:
        suits[card[1]] = suits.get(card[1], 0) + 1
    flush = max(suits.values()) >= 5

    #Check for Straight
    ranks = [rank_values[card[0]] for card in all_cards]
    ranks.sort()
    straight = False
    for i in range(len(ranks) - 4):
        if ranks[i+4] == ranks[i] + 4 and len(set(ranks[i:i+5])) == 5:
            straight = True
            break
    #Check for Ace-low straight
    if not straight and ranks == [2,3,4,5,14]:
        straight = True

    #Check for pairs, three of a kind, four of a kind, full house
    rank_counts = {}
    for rank, _ in all_cards:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1

    counts = sorted(rank_counts.values(), reverse=True)

    #Hand Ranking Logic (Improved)
    if straight and flush:
        return "Straight Flush", ranks[-1] #Added high card for tie-breaking
    if counts[0] == 4:
        return "Four of a Kind", ranks[0] #Added high card for tie-breaking
    if counts[0] == 3 and counts[1] == 2:
        return "Full House", ranks[0] #Added high card for tie-breaking
    if flush:
        return "Flush", ranks[-1] #Added high card for tie-breaking
    if straight:
        return "Straight", ranks[-1] #Added high card for tie-breaking
    if counts[0] == 3:
        return "Three of a Kind", ranks[0] #Added high card for tie-breaking
    if counts[0] == 2 and counts[1] == 2:
        return "Two Pair", ranks[0] #Added high card for tie-breaking
    if counts[0] == 2:
        return "Pair", ranks[0] #Added high card for tie-breaking
    return "High Card", ranks[-1] #Added high card for tie-breaking


def get_integer_input(prompt, min_val, max_val):
    """Gets integer input within a specified range, with error handling."""
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
    """Runs a poker simulation."""
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
            community_cards, hands = deal_cards(deck, num_players, hand_size, num_community_cards)
            print(f"\n--- Hand {hand_num} ---")
            print("\nCommunity cards:", display_hand(community_cards))
            hand_results = []
            for i, hand in enumerate(hands):
                hand_rank, high_card = evaluate_hand(hand, community_cards)
                print(f"Player {i+1}'s hand: {display_hand(hand)} ({hand_rank}, High Card: {ranks[high_card-2]})")
                hand_results.append((hand_rank, high_card, i))

            #Simple Winning Hand Determination (needs improvement for ties)
            winning_hand = max(hand_results, key=lambda x: (hand_rankings.index(x[0]), x[1]))
            print(f"\nPlayer {winning_hand[2]+1} wins with a {winning_hand[0]}!")

        except ValueError as e:
            print(f"Error dealing cards: {e}")
        print("-" * 20)

hand_rankings = ["High Card", "Pair", "Two Pair", "Three of a Kind", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush"]

if __name__ == "__main__":
    run_poker_simulation()
