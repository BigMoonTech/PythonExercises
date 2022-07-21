import unittest
import function_exercise as f

class FunctionTest(unittest.TestCase):

    def setUp(self):
        self.test_collection = [2, 4, 5, 7, 6, 3]


    def test_multiply_even_numbers(self):
        """return the result of multiplying all evens in a single list"""
        self.assertEqual(
            f.Function.multiply_even_numbers(self.test_collection),
            48
        )


    def test_multi_non_list_type(self):
        """raise errors for non-list types and lists with non-integers"""
        with self.assertRaises(TypeError):
            f.Function.multiply_even_numbers(dict({"key" : "value"})),
            "Argument must be a list of at least two integers"
        with self.assertRaises(TypeError):
            f.Function.multiply_even_numbers([1, "2", "b"]),
            "List must be integers"


    def test_return_day(self):
        """return None if day of week is outside of range 1 through 7, else return day"""
        self.assertEqual(
            f.Function.return_day(8),
            None
        )
        self.assertEqual(
            f.Function.return_day(2),
            "Monday"
        )


    def test_get_last_element(self):
        """return the last element in a list, if empty, return None"""
        self.assertEqual(f.Function.get_last_element(self.test_collection), 3)
        self.assertEqual(f.Function.get_last_element([]), None)


    def test_single_letter_count(self):
        """return the number of a specified letter in a word"""
        self.assertEqual(f.Function.single_letter_count("tobacco", "o"), 2)


    def test_multiple_letter_count(self):
        """return a dictionary with letters as keys and the letter count as values"""
        self.assertEqual(
            f.Function.multiple_letter_count("tear"),
            {
                "t" : 1,
                "e" : 1,
                "a" : 1,
                "r" : 1
            }
        )


if __name__ == "__main__":
    unittest.main()