import unittest
from aimysearch import search


class TestAiMySearch(unittest.TestCase):
    """test class of search.py
    """

    def test_run(self):
        """test method for run
        """
        target = "hogehoge"
        text = "hogehogaaaaaaaaaaaaaaaahogehoge"
        actual = search.AiMySearch(target, text).run()
        expected = [{'text': 'hogehogaaa', 'index': 0, 'length': 8}, {
            'text': 'aaahogehog', 'index': 20, 'length': 8}]
        self.assertEqual(expected, actual)
