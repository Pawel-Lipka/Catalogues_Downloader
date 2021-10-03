from unittest import mock,TestCase
from Main import Cataloge_downloader


class MyTestCase(TestCase):


    def test_sn_input(self):
        with mock.patch('builtins.input', return_value = 'test'):
            self.assertEqual(Cataloge_downloader.sn_input(self),'test')
    def test_log_in(selfs):
        pass
    def page_open(self):

if __name__ == '__main__':
    unittest.main()
