import unittest

class Test_sum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1,1,1,]), 3, "should be 3")

    def test_sum_tuple(self):
        self.assertEqual(sum((1,2,2)), 5 ,"should be 5")


if __name__ == "__main__" :
    unittest.main()