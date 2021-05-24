#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStringManipulation(Koan):
    "文字列操作"

    def test_use_format_to_interpolate_variables(self):
        "文字列の書式設定"
        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2)
        self.assertEqual("The values are one and 2", string)

    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        "置換フィールドはどんな順番でも何度でも使用できます"
        value1 = 'doh'
        value2 = 'DOH'
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        self.assertEqual("The values are DOH, doh, doh and DOH!", string)

    def test_any_python_expression_may_be_interpolated(self):
        "置換フィールドはどこにでも挿入できます"
        import math # math モジュールの追加 import a standard python module with math functions

        decimal_places = 4
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
            decimal_places)
        self.assertEqual("The square root of 5 is 2.2361", string)

    def test_you_can_get_a_substring_from_a_string(self):
        "部分文字列の抽出"
        string = "Bacon, lettuce and tomato"
        self.assertEqual('let', string[7:10])

    def test_you_can_get_a_single_character_from_a_string(self):
        "1文字だけ抽出"
        string = "Bacon, lettuce and tomato"
        self.assertEqual('a', string[1])

    def test_single_characters_can_be_represented_by_integers(self):
        "文字を Unicode 値に変換"
        self.assertEqual(97, ord('a'))
        self.assertEqual(True, ord('b') == (ord('a') + 1))

    def test_strings_can_be_split(self):
        "文字列の分割"
        string = "Sausage Egg Cheese"
        words = string.split()
        self.assertListEqual(["Sausage", "Egg", "Cheese"], words)

    def test_strings_can_be_split_with_different_patterns(self):
        "複数の区切り文字による文字列の分割"
        import re #import python regular expression library

        string = "the,rain;in,spain"
        pattern = re.compile(',|;')

        words = pattern.split(string)

        self.assertListEqual(['the', 'rain', 'in', 'spain'], words)

        # pattern は ',' か ';' にマッチする正規表現になっている
        # Pattern is a Python regular expression pattern which matches ',' or ';'

    def test_raw_strings_do_not_interpret_escape_characters(self):
        "raw 文字列では、エスケープ文字は認識されず、その文字そのものとなります"
        string = r'\n'
        self.assertNotEqual('\n', string)
        self.assertEqual('\\n', string)
        self.assertEqual(2, len(string))

        # Useful in regular expressions, file paths, URLs, etc.

    def test_strings_can_be_joined(self):
        "join メソッドによる文字列連結"
        words = ["Now", "is", "the", "time"]
        self.assertEqual("Now is the time", ' '.join(words))

    def test_strings_can_change_case(self):
        "大文字小文字の変換"
        self.assertEqual('Guido', 'guido'.capitalize())
        self.assertEqual('GUIDO', 'guido'.upper())
        self.assertEqual('timbot', 'TimBot'.lower())
        self.assertEqual('Guido Van Rossum', 'guido van rossum'.title())
        self.assertEqual('tOtAlLy AwEsOmE', 'ToTaLlY aWeSoMe'.swapcase())
