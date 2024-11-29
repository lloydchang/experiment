import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

def create_deck():
    """Creates a shuffled deck of cards."""
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_cards(deck, num_cards):
    """Deals cards from the deck and returns the hand and remaining deck."""
    if len(deck) < num_cards:
        raise ValueError("Not enough cards in the deck")
    hand = deck[:num_cards]
    remaining_deck = deck[num_cards:]
    return hand, remaining_deck

def display_hand(hand):
    """Displays a hand of cards in a user-friendly format."""
    return " ".join([f"{rank}{suit[0]}" for rank, suit in hand])

#Improved hand evaluation using a dedicated library.  Install with: pip install evaluator
from evaluator import evaluate_cards

def evaluate_hand(hand, community_cards):
    """Evaluates a hand using the evaluator library."""
    all_cards = [card[0] + card[1][0] for card in hand + community_cards]
    return evaluate_cards(all_cards)


def get_integer_input(prompt, min_val, max_val):
    """Gets integer input from the user within a specified range."""
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
    """Runs a Texas Hold'em poker simulation."""
    while True:
        try:
            num_players = get_integer_input("Enter the number of players (2-10): ", 2, 10)
            num_hands = get_integer_input("Enter the number of hands to simulate (1 or more): ", 1, 100)
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
            hand_evaluations = []
            for i, hand in enumerate(hands):
                evaluation = evaluate_hand(hand, community_cards)
                hand_evaluations.append((evaluation, hand))
                print(f"Player {i+1}'s hand: {display_hand(hand)} ({evaluation})")

            #Improved winning hand determination using the evaluator library
            winning_player = 0
            for i in range(1, num_players):
                if hand_evaluations[i][0] > hand_evaluations[winning_player][0]:
                    winning_player = i
            print(f"\nPlayer {winning_player + 1} wins!")

        except ValueError as e:
            print(f"Error dealing cards: {e}")
        print("-" * 20)

if __name__ == "__main__":
    run_poker_simulation()
