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
        raise ValueError(f"Not enough cards in the deck. Need {required_cards}, have {deck_size}.")

    community_cards = deck[:num_community_cards]
    player_hands = []
    start_index = num_community_cards
    for i in range(num_players):
        end_index = start_index + hand_size
        player_hands.append(deck[start_index:end_index])
        start_index = end_index
    return community_cards, player_hands


def main():
    """Main function to run the Texas Hold'em dealing simulation."""
    while True:
        try:
            num_players = int(input("Enter the number of players (2 or more): "))
            if num_players < 2:
                raise ValueError("You need at least two players.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    hand_size = 2
    num_community_cards = 5

    deck = create_deck()
    try:
        community_cards, hands = deal_cards(deck, num_players, hand_size, num_community_cards)
        print("\nCommunity cards:", community_cards)
        for i, hand in enumerate(hands):
            print(f"Player {i+1}'s hand: {hand}")
    except ValueError as e:
        print(f"Error dealing cards: {e}")


if __name__ == "__main__":
    main()
