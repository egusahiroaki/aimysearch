# coding:utf-8
# pylint: disable=C0111


import unittest
from aimysearch import search


class TestAiMySearch(unittest.TestCase):
    """test class of search.py
    """

    def test_run(self):
        """test method for run
        """
        target = "hogehoge"
        text = "hogehogfugafugapiyopihogehugepiyo"
        actual = search.AiMySearch(target, text).run()
        expected = [{'index': 0, 'length': 11, 'text': 'hogehogfuga'},
                    {'index': 17, 'length': 14, 'text': 'yopihogehugepi'}]
        self.assertEqual(expected, actual)

    def test_run_with_(self):
        """test method for run with high match rate
        """
        target = "hogehoge"
        text = "hogehogfugafugapiyopihogehugepiyo"
        actual = search.AiMySearch(target, text, 0, 0.8).run()
        expected = [{'index': 0, 'length': 8, 'text': 'hogehogf'},
                    {'index': 21, 'length': 8, 'text': 'hogehuge'}]
        self.assertEqual(expected, actual)
