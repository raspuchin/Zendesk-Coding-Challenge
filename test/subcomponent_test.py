import unittest
from src.subcomponent import subcomponent

class MyTestCase(unittest.TestCase):
    def test_length_one(self):
        sub = subcomponent()
        sub.set_display_str('Hello')
        self.assertEqual(sub.get_display(), 'Hello\n')

    def test_length_two(self):
        sub = subcomponent(10)
        sub.set_display_str('01234567890123456789')
        self.assertEqual(sub.get_display(), '0123456789\n0123456789\n')


if __name__ == '__main__':
    unittest.main()
