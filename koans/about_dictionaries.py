#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutHashes in the Ruby Koans
#

from runner.koan import *

class AboutDictionaries(Koan):
    "辞書（ディクショナリ）"

    def test_creating_dictionaries(self):
        "辞書 (dict) の作成"
        empty_dict = dict()
        self.assertEqual(dict, type(empty_dict))
        self.assertDictEqual({}, empty_dict)
        self.assertEqual(__, len(empty_dict))

    def test_dictionary_literals(self):
        "辞書の書き方"
        empty_dict = {}
        self.assertEqual(dict, type(empty_dict))
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        self.assertEqual(__, len(babel_fish))

    def test_accessing_dictionaries(self):
        "辞書の要素へのアクセス"
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        self.assertEqual(__, babel_fish['one'])
        self.assertEqual(__, babel_fish['two'])

    def test_changing_dictionaries(self):
        "辞書の要素の変更"
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        babel_fish['one'] = 'eins'

        expected = { 'two': 'dos', 'one': __ }
        self.assertDictEqual(expected, babel_fish)

    def test_dictionary_is_unordered(self):
        "辞書は順不同"
        dict1 = { 'one': 'uno', 'two': 'dos' }
        dict2 = { 'two': 'dos', 'one': 'uno' }

        self.assertEqual(__, dict1 == dict2)


    def test_dictionary_keys_and_values(self):
        "辞書のキーと値 (value)"
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(__, len(babel_fish.keys()))
        self.assertEqual(__, len(babel_fish.values()))
        self.assertEqual(__, 'one' in babel_fish.keys())
        self.assertEqual(__, 'two' in babel_fish.values())
        self.assertEqual(__, 'uno' in babel_fish.keys())
        self.assertEqual(__, 'dos' in babel_fish.values())

    def test_making_a_dictionary_from_a_sequence_of_keys(self):
        "キーのシーケンスから同じ値を持つ辞書を作成"
        cards = {}.fromkeys(('red warrior', 'green elf', 'blue valkyrie', 'yellow dwarf', 'confused looking zebra'), 42)

        self.assertEqual(__, len(cards))
        self.assertEqual(__, cards['green elf'])
        self.assertEqual(__, cards['yellow dwarf'])

