import unittest
import os

from APIGetCSVWrite.src import APIHelper


class TestAPI(unittest.TestCase):

    def _setUp(self, url):
        self.obj = APIHelper.APIHelper(url)

    def tearDown(self):
        pass

    def test_responseNotEmpty(self):
        url = "https://swapi.dev/api/people/"
        o_file_name = 'output_001.csv'

        self._setUp(url)
        api_o = self.obj.star_wars_characters()
        self.obj.append_to_file(o_file_name)
        assert type(api_o) is list
        assert len(api_o) != 0


if __name__ == '__main__':
    unittest.main()
