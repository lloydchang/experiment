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

def evaluate_hand(hand, community_cards):
    """Evaluates a hand and returns the hand rank and high cards for tie-breaking."""
    all_cards = sorted(hand + community_cards, key=lambda x: rank_values[x[0]])

    #Flush Check
    suits = {}
    for card in all_cards:
        suits[card[1]] = suits.get(card[1], 0) + 1
    flush = max(suits.values()) >= 5

    #Straight Check
    ranks = [rank_values[card[0]] for card in all_cards]
    ranks.sort()
    straight = False
    for i in range(len(ranks) - 4):
        if ranks[i+4] == ranks[i] + 4 and len(set(ranks[i:i+5])) == 5:
            straight = True
            break
    #Ace-low straight check
    if not straight and ranks == [2,3,4,5,14]:
        straight = True

    #Pair, Three of a Kind, Four of a Kind, Full House Check
    rank_counts = {}
    for rank, _ in all_cards:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    counts = sorted(rank_counts.values(), reverse=True)

    #Hand Ranking Logic
    if straight and flush:
        return "Straight Flush", ranks[1:]
    if counts[0] == 4:
        return "Four of a Kind", ranks[:4]
    if counts[0] == 3 and counts[1] == 2:
        return "Full House", ranks[:3] + ranks[3:5]
    if flush:
        return "Flush", ranks[1:]
    if straight:
        return "Straight", ranks[1:]
    if counts[0] == 3:
        return "Three of a Kind", ranks[:3]
    if counts[0] == 2 and counts[1] == 2:
        return "Two Pair", ranks[:4]
    if counts[0] == 2:
        return "Pair", ranks[:2]
    return "High Card", ranks[1:]


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

    hand_rankings = ["High Card", "Pair", "Two Pair", "Three of a Kind", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush"]

    for hand_num in range(1, num_hands + 1):
        deck = create_deck()
        try:
            community_cards, hands = deal_cards(deck, num_players, hand_size, num_community_cards)
            print(f"\n--- Hand {hand_num} ---")
            print("\nCommunity cards:", display_hand(community_cards))
            hand_results = []
            for i, hand in enumerate(hands):
                hand_rank, high_cards = evaluate_hand(hand, community_cards)
                print(f"Player {i+1}'s hand: {display_hand(hand)} ({hand_rank}, High Cards: {[ranks[card-2] for card in high_cards]})")
                hand_results.append((hand_rank, high_cards, i))

            #Winning Hand Determination (Handles ties)
            winning_hands = []
            best_rank_index = float('inf')
            for hand_rank, high_cards, player_index in hand_results:
                rank_index = hand_rankings.index(hand_rank)
                if rank_index < best_rank_index:
                    winning_hands = [(hand_rank, high_cards, player_index)]
                    best_rank_index = rank_index
                elif rank_index == best_rank_index:
                    winning_hands.append((hand_rank, high_cards, player_index))

            winning_player_indices = [player_index for _, _, player_index in winning_hands]
            winning_players_str = ", ".join(map(str, [index + 1 for index in winning_player_indices]))

            if len(winning_hands) > 1:
                print("\nTie between players:", winning_players_str)
                #Tie-breaker logic
                winning_hands.sort(key=lambda x: x[1], reverse=True)
                print(f"\nPlayer {winning_hands[0][2]+1} wins the tie with a {winning_hands[0][0]}!")

            else:
                print(f"\nPlayer {winning_hands[0][2]+1} wins with a {winning_hands[0][0]}!")

        except ValueError as e:
            print(f"Error dealing cards: {e}")
        print("-" * 20)

if __name__ == "__main__":
    run_poker_simulation()
