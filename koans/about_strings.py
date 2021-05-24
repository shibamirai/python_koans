#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStrings(Koan):
    "文字列"

    def test_double_quoted_strings_are_strings(self):
        "ダブルクォーテーションで囲まれたものは文字列です"
        string = "Hello, world."
        self.assertEqual(True, isinstance(string, str))

    def test_single_quoted_strings_are_also_strings(self):
        "シングルクォーテーションで囲まれたものも文字列です"
        string = 'Goodbye, world.'
        self.assertEqual(True, isinstance(string, str))

    def test_triple_quote_strings_are_also_strings(self):
        "トリプルクォーテーションで囲まれたものも文字列です"
        string = """Howdy, world!"""
        self.assertEqual(True, isinstance(string, str))

    def test_triple_single_quotes_work_too(self):
        "トリプルシングルクォーテーションで囲まれたものも文字列です"
        string = '''Bonjour tout le monde!'''
        self.assertEqual(True, isinstance(string, str))

    def test_raw_strings_are_also_strings(self):
        "raw 文字列も文字列です"
        string = r"Konnichi wa, world!"
        self.assertEqual(True, isinstance(string, str))

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        "ダブルクォーテーションを含む文字列はシングルクォーテーションで囲みます"
        string = 'He said, "Go Away."'
        self.assertEqual('He said, "Go Away."', string)

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        "シングルクォーテーションを含む文字列はダブルクォーテーションで囲みます"
        string = "Don't"
        self.assertEqual("Don't", string)

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        "クォーテーションを文字として使う場合は、バックスラッシュ(\)でエスケープします"
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        self.assertEqual(True, (a == b))

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        "文字列を次の行に続けるには、行末にバックスラッシュを使います"
        string = "It was the best of times,\n\
It was the worst of times."
        self.assertEqual(52, len(string))

    def test_triple_quoted_strings_can_span_lines(self):
        "トリプルクォーテーションで複数行にわたる文字列が作れます"
        string = """
Howdy,
world!
"""
        self.assertEqual(15, len(string))

    def test_triple_quoted_strings_need_less_escaping(self):
        "トリプルクォーテーションではクォーテーションのエスケープが不要です"
        a = "Hello \"world\"."
        b = """Hello "world"."""
        self.assertEqual(True, (a == b))

    def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
        "トリプルクォーテーションでも行末のクォーテーションはエスケープしなければなりません"
        string = """Hello "world\""""
        self.assertEqual('Hello "world"', string)

    def test_plus_concatenates_strings(self):
        "+ で文字列を結合します"
        string = "Hello, " + "world"
        self.assertEqual("Hello, world", string)

    def test_adjacent_strings_are_concatenated_automatically(self):
        "隣接した文字列は自動的に結合されます"
        string = "Hello" ", " "world"
        self.assertEqual("Hello, world", string)

    def test_plus_will_not_modify_original_strings(self):
        "+ は元の文字列を変更しません"
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual("Hello, ", hi)
        self.assertEqual("world", there)

    def test_plus_equals_will_append_to_end_of_string(self):
        "+= は元の文字列の末尾に結合します"
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual("Hello, world", hi)

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        "+= も元の文字列は変更しません"
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual("Hello, ", original)

    def test_most_strings_interpret_escape_characters(self):
        "どのタイプの文字列でも改行等のエスケープ文字が使えます"
        string = "\n"
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        self.assertEqual(1, len(string))
