
class Function:

    @staticmethod
    def multiply_even_numbers(collection):
        """
        Multiplies the even numbers in a single list
        :param collection: a list of at least two integers
        :return: the total
        """
        # throw error if any element in the collection isn't an int
        for i in collection:
            if not type(i) is int:
                raise TypeError("List must be integers")

        # throw error if collection is not a list or if less than two ints
        if isinstance(collection, list) and len(collection) > 1:
                elm_x = [elm for elm in collection if elm % 2 == 0]
                total = collection[0]
                for i in elm_x[1:]:
                    total *= i
                return total
        else:
            raise TypeError("Argument must be a list of at least two integers")

    @staticmethod
    def return_day(val):
        days = {
            1 : "Sunday",
            2 : "Monday",
            3 : "Tuesday",
            4 : "Wednesday",
            5 : "Thursday",
            6 : "Friday",
            7 : "Saturday"
        }

        if 1 <= val <=7:
            return days[val]
        else:
            return None

    @staticmethod
    def get_last_element(collection):
        if len(collection) > 0:
            return collection[-1]
        else:
            return None

    @staticmethod
    def single_letter_count(word, letter):
        """counts the letters in a word"""
        char_list = [char for char in word.lower()]
        return char_list.count(letter)

    @staticmethod
    def multiple_letter_count(word):
        """
        separates a word into a dict with letters as K and the count of that letter as V
        :param word: one word
        :return: dict
        """
        li = {letter: word.count(letter) for letter in word.lower()}
        return li
    