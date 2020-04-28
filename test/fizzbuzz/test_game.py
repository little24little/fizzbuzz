from unittest import TestCase
from src.fizzbuzz.game import count_off


class TestCountOff(TestCase):

    def test_index_is_1_return_1(self):
        self.assertEqual('1', count_off(1))

    def test_when_index_is_3_return_fizz(self):
        self.assertEqual('Fizz', count_off(3))

    def test_when_index_is_5_return_buzz(self):
        self.assertEqual('Buzz', count_off(5))

    def test_when_index_is_7_return_buzz(self):
        self.assertEqual('Whizz', count_off(7))

    def test_when_index_is_3_5_7_multiple_return_correct_result(self):
        self.assertEqual('FizzBuzz', count_off(60))
        self.assertEqual('FizzWhizz', count_off(21))
        self.assertEqual('FizzBuzzWhizz', count_off(210))

    def test_when_index_contains_3_return_fizz(self):
        self.assertEqual('Fizz', count_off(33))
        self.assertEqual('Fizz', count_off(13))
        self.assertEqual('Fizz', count_off(103))

    def test_when_index_contains_5_return_correct_result(self):
        self.assertEqual('Buzz', count_off(25))
        self.assertEqual('BuzzWhizz', count_off(35))

    def test_when_index_contains_7_return_correct_result(self):
        self.assertEqual('17', count_off(17))
        self.assertEqual('Fizz', count_off(75))
