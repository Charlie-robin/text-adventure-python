import unittest

from view.TextFormatter import TextFormatter

class TestTextFormatter(unittest.TestCase):

    # _validate_length()

    def test_validate_length_raises_exception_when_text_larger_then_line_width(self):
        with self.assertRaises(Exception):
            TextFormatter._validate_length("hello", 2)     

    # pad_text()

    def test_pad_text_matches_default_end_character(self):
        result = TextFormatter.pad_text("hello", 10)
        self.assertEqual(result, "* hello  *")

    def test_pad_text_matches_given_end_character(self):
        result = TextFormatter.pad_text("hello", 10, "!")
        self.assertEqual(result, "! hello  !")    

    def test_pad_text_matches_specified_length(self):
        result = TextFormatter.pad_text("hello", 20)
        self.assertEqual(len(result), 20)    

    # center_pad()    

    def test_center_pad_text_matches_specified_length(self):
        result = TextFormatter.center_pad_text("hi", 50)
        self.assertEqual(len(result),50)

    def test_center_pad_text_handles_even_text(self):
        result = TextFormatter.center_pad_text("hi", 10)
        self.assertEqual(result,"*   hi   *")

    def test_center_pad_text_handles_odd_text(self):
        result = TextFormatter.center_pad_text("hello", 10)
        self.assertEqual(result,"* hello  *")

    def test_center_pad_text_matches_default_end_character(self):
        result = TextFormatter.center_pad_text("hi", 10)
        self.assertEqual(result,"*   hi   *")

    def test_center_pad_text_given_end_character(self):
        result = TextFormatter.center_pad_text("hi", 10, "|")
        self.assertEqual(result,"|   hi   |")  

    # split_oversized_text

    def test_split_oversized_text_divides_into_three_strings(self):
        result = TextFormatter.split_oversized_text("hello hello hello", 5)
        self.assertEqual(result, ["hello", "hello", "hello"])

    def test_split_oversized_text_divides_into_two_strings(self):
        result = TextFormatter.split_oversized_text("hello hello hello", 20)
        self.assertEqual(result, ["hello hello", "hello"])    

    def test_split_oversized_text_divides_into_one_string(self):
        result = TextFormatter.split_oversized_text("hello hello hello", 50)
        self.assertEqual(result, ["hello hello hello"])   

if __name__ == "__main__":
    unittest.main()
