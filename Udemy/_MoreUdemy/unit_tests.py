import unittest
from activities import eat, nap

class ActivityTests(unittest.TestCase):

    def test_eat_healthy(self):
        self.assertEqual(
            eat("salad", is_healthy=True),
            "I'm eating salad, because it is healthy"
        )


    def test_eat_unhealthy(self):
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because I don't care about my body right now"
        )


    def test_short_nap(self):
        self.assertEqual(
            nap(1),
            "I love this length of nap"
        )


    def test_long_nap(self):
        self.assertEqual(
            nap(3),
            "I napped for too long and now I feel more tired"
        )


    def test_invalid_nap(self):
        self.assertEqual(
            nap(-1),
            "Can't have a negative/zero nap!"
        )


if __name__ == "__main__":
    unittest.main()