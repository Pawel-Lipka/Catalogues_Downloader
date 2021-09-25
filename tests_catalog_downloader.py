import unittest
from Main import Cataloge_downloader

class MyTestCase(unittest.TestCase):
    def test_sn_input(self):
        self.assertEqual(Cataloge_downloader.sn_input())
if __name__ == '__main__':
    unittest.main()
