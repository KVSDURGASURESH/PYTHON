import unittest
import os

from APIGetCSVWrite.src import APIHelper


class TestAPI(unittest.TestCase):

    def _setUp(self, url, o_file_name):
        self.obj = APIHelper.APIHelper(url)
        self.obj.append_to_file(o_file_name)

    def tearDown(self):
        pass

    def test_responseNotEmpty(self):
        url = "https://swapi.dev/api/people/"
        o_file_name = 'output_001.csv'

        self._setUp(url, o_file_name)
        api_o = self.obj.star_wars_characters()
        assert type(api_o) is list
        assert len(api_o) != 0


if __name__ == '__main__':
    unittest.main()
