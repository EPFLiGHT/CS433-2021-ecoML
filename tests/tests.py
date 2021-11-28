import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_2(self):
        self.assertEqual(1, 2)  # add assertion here


if __name__ == '__main__':
    unittest.main()
