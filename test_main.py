import unittest
from main import create_deck, deal_cards, evaluate_hand

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
        community_cards = [("K", "Clubs"), ("Q", "Spades"), ("Q", "Hearts"), ("2", "Clubs")] #Missing a card
        evaluation = evaluate_hand(hand, community_cards)
        self.assertIsNone(evaluation) #Expect None due to error


if __name__ == '__main__':
    unittest.main()
