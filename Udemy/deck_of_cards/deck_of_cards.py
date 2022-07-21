from random import shuffle


class Card:
    
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:


    def __init__(self):
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(value, suit) for suit in suits for value in values]

    
    def __iter__(self):
        """
        This allows the Deck class to be iterated through
        :return: None
        """
        return iter(self.cards)


    def __repr__(self):
        return "Deck of {} cards".format(self.count())


    def count(self):
        return len(self.cards)

    
    def _deal(self, number):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        else:
            hand = []
            while number > 0:
                if self.count() > 0:
                    hand.append(self.cards.pop())
                number -= 1
        return hand


    def deal_card(self):
        return self._deal(1)[0]


    def deal_hand(self, number):
        return self._deal(number)

    def shuffle_new_deck(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self



deck = Deck()
print(deck.cards)
deck.shuffle_new_deck()
print(deck.cards)
card = deck.deal_card()
print(card)
print(deck.count())
hand = deck.deal_hand(26)
print(deck.count())
print(hand)
print(deck.cards)

# by calling iter on deck we can loop through the iterator and print every card
for card in deck:
    print(card)

