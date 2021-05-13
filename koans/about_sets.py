#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutSets(Koan):
    "セット（集合）"

    def test_sets_make_keep_lists_unique(self):
        "セットはリストの要素の重複をなくします"
        highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas', 'MacLeod', 'Malcolm', 'MacLeod']

        there_can_only_be_only_one = set(highlanders)

        self.assertEqual(__, there_can_only_be_only_one)

    def test_empty_sets_have_different_syntax_to_populated_sets(self):
        "空のセットの書き方"
        self.assertEqual(__, {1, 2, 3})
        self.assertEqual(__, set())

    def test_dictionaries_and_sets_use_same_curly_braces(self):
        "辞書型とセット型は同じ波カッコ{}を使います"
        # 注意：波かっこを使った書き方は python 3 から導入され、python 2.7 にも移植されました
        # Note: Literal sets using braces were introduced in python 3.
        #       They were also backported to python 2.7.

        self.assertEqual(__, {1, 2, 3}.__class__)
        self.assertEqual(__, {'one': 1, 'two': 2}.__class__)

        self.assertEqual(__, {}.__class__)

    def test_creating_sets_using_strings(self):
        "文字列から作るセット"
        self.assertEqual(__, {'12345'})
        self.assertEqual(__, set('12345'))

    def test_convert_the_set_into_a_list_to_sort_it(self):
        "セットをソートするとリストになります"
        self.assertEqual(__, sorted(set('12345')))

    # ------------------------------------------------------------------

    def test_set_have_arithmetic_operators(self):
        "セットは集合演算が可能です"
        scotsmen = {'MacLeod', 'Wallace', 'Willie'}
        warriors = {'MacLeod', 'Wallace', 'Leonidas'}

        self.assertEqual(__, scotsmen - warriors)
        self.assertEqual(__, scotsmen | warriors)
        self.assertEqual(__, scotsmen & warriors)
        self.assertEqual(__, scotsmen ^ warriors)

    # ------------------------------------------------------------------

    def test_we_can_query_set_membership(self):
        "セットは要素の存在確認ができます"
        self.assertEqual(__, 127 in {127, 0, 0, 1} )
        self.assertEqual(__, 'cow' not in set('apocalypse now') )

    def test_we_can_compare_subsets(self):
        "セット同士で、部分集合になっているか判定できます"
        self.assertEqual(__, set('cake') <= set('cherry cake'))
        self.assertEqual(__, set('cake').issubset(set('cherry cake')) )

        self.assertEqual(__, set('cake') > set('pie'))
