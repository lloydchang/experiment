import random
import unittest

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_cards(deck, num_cards):
    if len(deck) < num_cards:
        raise ValueError(f"Not enough cards in the deck to deal {num_cards} cards.")
    hand, remaining_deck = deck[:num_cards], deck[num_cards:]
    return hand, remaining_deck

def display_hand(hand):
    return " ".join([f"{rank}{suit[0]}" for rank, suit in hand])

#Improved hand evaluation using a dedicated library.  Install with: pip install evaluator
from evaluator import evaluate_cards

def evaluate_hand(hand, community_cards):
    all_cards = [card[0] + card[1][0] for card in hand + community_cards]
    try:
        return evaluate_cards(all_cards)
    except Exception as e:
        print(f"Error evaluating hand: {e}. Check your evaluator library installation and version.")
        return None

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
            print(f"Invalid input: {e}. Please try again.")

def play_hand(num_players, hand_size, num_community_cards):
    deck = create_deck()
    community_cards = []
    hands = []
    try:
        remaining_deck = deck
        for _ in range(num_players):
            hand, remaining_deck = deal_cards(remaining_deck, hand_size)
            hands.append(hand)

        flop, remaining_deck = deal_cards(remaining_deck, 3)
        community_cards.extend(flop)
        turn, remaining_deck = deal_cards(remaining_deck, 1)
        community_cards.extend(turn)
        river, remaining_deck = deal_cards(remaining_deck, 1)
        community_cards.extend(river)

        hand_evaluations = []
        for hand in hands:
            evaluation = evaluate_hand(hand, community_cards)
            if evaluation is not None:
                hand_evaluations.append((evaluation, hand))
            else:
                hand_evaluations.append((None, hand)) #Append None for error handling

        return hands, community_cards, hand_evaluations

    except ValueError as e:
        print(f"Error dealing cards: {e}")
        return None, None, None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None, None


def determine_winner(hand_evaluations):
    if not hand_evaluations:
        return None
    winning_player = 0
    winning_hand_rank = hand_evaluations[0][0]
    for i in range(1, len(hand_evaluations)):
        if hand_evaluations[i][0] is not None and hand_evaluations[i][0] > winning_hand_rank:
            winning_hand_rank = hand_evaluations[i][0]
            winning_player = i
    return winning_player, winning_hand_rank


def run_poker_simulation(num_players, num_hands):
    hand_size = 2
    num_community_cards = 5
    results = []
    for _ in range(num_hands):
        hands, community_cards, hand_evaluations = play_hand(num_players, hand_size, num_community_cards)
        if hands and community_cards and hand_evaluations:
            winner, winning_hand = determine_winner(hand_evaluations)
            results.append((hands, community_cards, hand_evaluations, winner, winning_hand))
    return results


def main():
    while True:
        try:
            num_players = get_integer_input("Enter the number of players (2-10): ", 2, 10)
            num_hands = get_integer_input("Enter the number of hands to simulate (1 or more): ", 1, 1000)
            break
        except ValueError as e:
            print(f"Error: {e}")
            continue
    results = run_poker_simulation(num_players, num_hands)
    for i, (hands, community_cards, hand_evaluations, winner, winning_hand) in enumerate(results):
        print(f"\n--- Hand {i+1} ---")
        print("\nCommunity cards:", display_hand(community_cards))
        for j, hand in enumerate(hands):
            evaluation = hand_evaluations[j][0]
            print(f"Player {j+1}'s hand: {display_hand(hand)} {'('+str(evaluation)+')' if evaluation is not None else '(Error evaluating hand)'}")
        if winner is not None:
            print(f"\nPlayer {winner + 1} wins with a {winning_hand}!")
        else:
            print("\nNo hands could be evaluated.")
        print("-" * 20)


class TestPokerGame(unittest.TestCase):
    def test_create_deck(self):
        deck = create_deck()
        self.assertEqual(len(deck), 52)

    def test_deal_cards(self):
        deck = create_deck()
        hand, remaining_deck = deal_cards(deck, 5)
        self.assertEqual(len(hand), 5)
        self.assertEqual(len(remaining_deck), 47)

    def test_evaluate_hand_full_house(self):
        hand = [("K", "Hearts"), ("K", "Diamonds")]
        community_cards = [("K", "Clubs"), ("Q", "Spades"), ("Q", "Hearts"), ("2", "Clubs"), ("A", "Diamonds")]
        evaluation = evaluate_hand(hand, community_cards)
        self.assertEqual(evaluation, 7) #Full House

    def test_evaluate_hand_error(self):
        hand = [("K", "Hearts"), ("K", "Diamonds")]
        community_cards = [("K", "Clubs"), ("Q", "Spades"), ("Q", "Hearts"), ("2", "Clubs"), ("A", "Diamonds")]
        #Simulate an error in the evaluator library
        try:
            from evaluator import evaluate_cards
            evaluate_cards("invalid input")
            self.fail("Expected exception not raised")
        except Exception as e:
            self.assertTrue(True) #Expect an exception


    def test_determine_winner(self):
        hand_evaluations = [(8, ["A", "K"]), (7, ["Q", "J"])]
        winner, winning_hand = determine_winner(hand_evaluations)
        self.assertEqual(winner, 0)
        self.assertEqual(winning_hand, 8)

        hand_evaluations = [(7, ["A", "K"]), (7, ["Q", "J"])]
        winner, winning_hand = determine_winner(hand_evaluations)
        self.assertEqual(winner, 0)
        self.assertEqual(winning_hand, 7)

        hand_evaluations = [(None, ["A", "K"]), (7, ["Q", "J"])]
        winner, winning_hand = determine_winner(hand_evaluations)
        self.assertEqual(winner, 1)
        self.assertEqual(winning_hand, 7)

        hand_evaluations = [(None, ["A", "K"]), (None, ["Q", "J"])]
        winner, winning_hand = determine_winner(hand_evaluations)
        self.assertIsNone(winner)
        self.assertIsNone(winning_hand)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False) #Run tests

