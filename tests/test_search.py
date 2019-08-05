# coding:utf-8
# pylint: disable=C0111


import unittest
from collections import namedtuple
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

    def test_initialize(self):
        """test method for constructor
        """
        target = "hogehoge"
        text = "hogehogfugafugapiyopihogehugepiyo"

        testCase = namedtuple(
            "testcase", "msg match_rate is_error")
        test_cases = [
            testCase(msg="with lower", match_rate=0, is_error=True),
            testCase(msg="", match_rate=0.5, is_error=False),
            testCase(msg="with upper", match_rate=1, is_error=True),
        ]

        for case in test_cases:
            with self.subTest(msg=case.msg):
                if case.is_error:
                    with self.assertRaises(search.AiMySearch.MatchRateError):
                        search.AiMySearch(target, text, 0, case.match_rate)
                else:
                    self.assertIsInstance(search.AiMySearch(
                        target, text, 0, case.match_rate), search.AiMySearch)

    def test_run2(self):
        """test method for run with high match rate
        """
        target = "hogehoge"
        text = "hogehogfugafugapiyopihogehugepiyo"
        actual = search.AiMySearch(target, text, 0, 0.8).run()
        expected = [{'index': 0, 'length': 8, 'text': 'hogehogf'},
                    {'index': 21, 'length': 8, 'text': 'hogehuge'}]
        self.assertEqual(expected, actual)

    def test_run3(self):
        """test method for run with no text
        """
        target = "hogehoge"
        text = ""
        with self.assertRaises(search.AiMySearch.TargetTextError):
            search.AiMySearch(target, text, 0, 0.8)

    def test_run4(self):
        """test method for run
        """
        target = "hoge"
        text = "aaaahhooaaaa"
        actual = search.AiMySearch(target, text, 0, 0.8).run()
        expected = [{'index': 4, 'length': 4, 'text': 'hhoo'}]
        self.assertEqual(expected, actual)

    def test_run5(self):
        """test method for run
        """
        target = "hoge"
        text = "aaaaohohaaaa"
        actual = search.AiMySearch(target, text, 0, 0.8).run()
        expected = [{'index': 4, 'length': 4, 'text': 'ohoh'}]
        self.assertEqual(expected, actual)
