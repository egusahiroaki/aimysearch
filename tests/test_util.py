import unittest
from aimysearch.util import n_gram


class TestUtil(unittest.TestCase):
    def test_n_gram(self):
        target = "hogefuga"
        actual = n_gram(target, 2)
        expected = [{'index': 0, 'length': 2, 'text': 'ho'},
                    {'index': 1, 'length': 2, 'text': 'og'},
                    {'index': 2, 'length': 2, 'text': 'ge'},
                    {'index': 3, 'length': 2, 'text': 'ef'},
                    {'index': 4, 'length': 2, 'text': 'fu'},
                    {'index': 5, 'length': 2, 'text': 'ug'},
                    {'index': 6, 'length': 2, 'text': 'ga'}]
        self.assertEqual(expected, actual)
