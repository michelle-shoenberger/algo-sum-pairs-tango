from sum_pairs import sum_pairs
import unittest

class SumPairsTester(unittest.TestCase):

    test_numbers = [1, 2, 3, 4, 5]
    test_sum = 7
    test_answer = [[3,4], [2,5]]

    def test_return(self):
        """ This tests that function returns a value"""
        self.assertIsNotNone(sum_pairs(self.test_numbers, self.test_sum))

    def test_simple_case(self):
        """Tests that returns one pair from one that equals sum"""
        self.assertEqual(sum_pairs([0,1], 1), [[0,1]])

    def test_more_complex(self):
        """Tests that returns two pairs"""
        self.assertEqual(sum_pairs([3,1,5,8,2], 27), "Unable to find pairs")

    def test_no_answer(self):
        """Tests that returns unable if no pairs"""
        self.assertEqual(sum_pairs(self.test_numbers, self.test_sum), self.test_answer)

if __name__ == "__main__":
    unittest.main()