import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_cards(deck, num_players, hand_size, num_community_cards):
    """Deals cards for Texas Hold'em."""
    if len(deck) < num_players * hand_size + num_community_cards:
        raise ValueError("Not enough cards in the deck for the specified number of players and community cards.")

    community_cards = deck[:num_community_cards]
    remaining_deck = deck[num_community_cards:]
    hands = []
    for i in range(num_players):
        hands.append(remaining_deck[i * hand_size:(i + 1) * hand_size])
    return community_cards, hands


def main():
    num_players = int(input("Enter the number of players: "))
    if num_players < 2:
        print("You need at least two players to play Texas Hold'em.")
        return

    hand_size = 2
    num_community_cards = 5

    deck = create_deck()
    community_cards, hands = deal_cards(deck, num_players, hand_size, num_community_cards)

    print("Community cards:", community_cards)
    for i, hand in enumerate(hands):
        print(f"Player {i+1}'s hand: {hand}")

if __name__ == "__main__":
    main()
