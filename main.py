import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def create_deck():
    """Creates a shuffled deck of cards."""
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_cards(deck, num_players, hand_size, num_community_cards):
    """Deals cards to players and the community."""
    deck_size = len(deck)
    required_cards = num_players * hand_size + num_community_cards
    if deck_size < required_cards:
        raise ValueError(f"Not enough cards in the deck to deal to {num_players} players. Need {required_cards}, have {deck_size}.")

    community_cards = deck[:num_community_cards]
    player_hands = []
    start_index = num_community_cards
    for i in range(num_players):
        end_index = start_index + hand_size
        player_hands.append(deck[start_index:end_index])
        start_index = end_index
    return community_cards, player_hands


def display_hand(hand):
    """Displays a hand of cards in a user-friendly format."""
    return " ".join([f"{rank}{suit[0]}" for rank, suit in hand])


def get_num_players():
    """Gets the number of players from the user with input validation."""
    while True:
        try:
            num_players_str = input("Enter the number of players (2-10): ")
            num_players = int(num_players_str)
            if 2 <= num_players <= 10:
                return num_players
            else:
                raise ValueError("Number of players must be between 2 and 10.")
        except ValueError as e:
            print(f"Invalid input: {e}")

def get_num_hands():
    """Gets the number of hands to deal from the user with input validation."""
    while True:
        try:
            num_hands_str = input("Enter the number of hands to deal (1 or more): ")
            num_hands = int(num_hands_str)
            if num_hands >= 1:
                return num_hands
            else:
                raise ValueError("Number of hands must be at least 1.")
        except ValueError as e:
            print(f"Invalid input: {e}")


def main():
    """Main function to run the Texas Hold'em dealing simulation."""
    num_players = get_num_players()
    num_hands = get_num_hands()
    hand_size = 2
    num_community_cards = 5

    for hand_num in range(1, num_hands + 1):
        deck = create_deck()
        try:
            community_cards, hands = deal_cards(deck, num_players, hand_size, num_community_cards)
            print(f"\n--- Hand {hand_num} ---")
            print("\nCommunity cards:", display_hand(community_cards))
            for i, hand in enumerate(hands):
                print(f"Player {i+1}'s hand: {display_hand(hand)}")
        except ValueError as e:
            print(f"Error dealing cards: {e}")
        print("-" * 20)


if __name__ == "__main__":
    main()
