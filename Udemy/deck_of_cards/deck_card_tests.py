import unittest
import deck_of_cards as card_deck

class CardTests(unittest.TestCase):

    def setUp(self) -> None:
        self.card = card_deck.Card("A", "Spades")

    def test_card_init(self):
        """Card should have a suit and a value"""
        self.assertEqual(self.card.suit, "Spades")
        self.assertEqual(self.card.value, "A")

    def test_card_repr(self):
        """Should print 'A of Spades'"""
        self.assertEqual(
            repr(self.card),
            "A of Spades"
        )

class DeckTests(unittest.TestCase):

    def setUp(self) -> None:
        self.deck = card_deck.Deck()


    def test_deck_init(self):
        """Deck should have a cards attribute which is a list 52 in length"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)


    def test_deck_iter(self):
        """Deck should be iterable so we can print every card"""
        try:
            iter(self.deck)
        except TypeError:
            self.fail(f'{self.deck!r} expected to be iterable')


    def test_deck_repr(self):
        """Should print 'Deck of 52 cards'"""
        self.assertEqual(
            repr(self.deck),
            "Deck of 52 cards"
        )


    def test_count(self):
        """length of a new deck should be 52"""
        self.assertEqual(self.deck.count(), 52)


    def test_deal_sufficient_cards(self):
        """deal cards from the deck if the requested number of cards is less than the deck size"""
        cards = self.deck.deal_hand(11)
        self.assertEqual(
            self.deck.count() + len(cards),
            52
        )


    def test_deal_insufficient_cards(self):
        """should deal the remaining number of cards left in the deck and ValueError if no cards in deck"""
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)
        with self.assertRaises(ValueError):
            self.deck._deal(1),
            "ValueError: All cards have been dealt"


    def test_deal_card(self):
        """deal one card, and card should equal the last item in self.deck.cards before it was dealt"""
        top_card = self.deck.cards[-1]
        card = self.deck.deal_card()
        self.assertEqual(card, top_card)


    def test_deal_hand(self):
        """remove the number of specified cards from the deck"""
        cards = self.deck.deal_hand(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(len(self.deck.cards), 42)


    def test_shuffle_new_deck(self):
        """should shuffle the deck if deck is full"""
        cards = self.deck.cards[:]
        self.assertNotEqual(self.deck.shuffle_new_deck(), cards)


    def test_shuffle_light_deck(self):
        """when attempting to shuffle a deck that is not full, raise ValueError"""
        self.deck.cards.pop()
        with self.assertRaises(ValueError):
            self.deck.shuffle_new_deck(),
            "Only full decks can be shuffled"


if __name__ == "__main__":
    unittest.main()