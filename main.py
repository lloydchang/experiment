import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_hand(deck, num_players, hand_size):
    hands = []
    for i in range(num_players):
        hands.append(deck[i*hand_size:(i+1)*hand_size])
    return hands

def main():
    deck = create_deck()
    num_players = 2
    hand_size = 2
    hands = deal_hand(deck, num_players, hand_size)
    for i, hand in enumerate(hands):
        print(f"Player {i+1}'s hand: {hand}")

if __name__ == "__main__":
    main()

