import unittest
from src.screen import screen
from src.subcomponent import subcomponent

class screen_test(unittest.TestCase):
    def test_one(self):
        scr = screen()
        sub = scr.display_error('error time')[0]
        self.assertEqual(sub.get_display(), 'Error: error time')


if __name__ == '__main__':
    unittest.main()
