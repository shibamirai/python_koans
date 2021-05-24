#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutAsserts(Koan):
    "assert の使い方"

    def test_assert_truth(self):
        "真実の主張"
        """
        私たちは assert を使って解答内容を調べ、採点します
        We shall contemplate truth by testing reality, via asserts.
        """

        # よくわからなければこの動画を見てください
        # Confused? This video should help:
        #
        #   http://bit.ly/about_asserts

        self.assertTrue(True) # ここは True であるべきです

    def test_assert_with_message(self):
        "メッセージ付きの主張"
        """
        適切なメッセージがあれば、もっと解きやすいでしょう
        Enlightenment may be more easily achieved with appropriate messages.
        """
        self.assertTrue(True, "ここは True であるべきです -- 修正してください")

    def test_fill_in_values(self):
        "値の入力"
        """
        値を入力してもらうこともあります
        Sometimes we will ask you to fill in the values
        """
        self.assertEqual(2, 1 + 1)

    def test_assert_equality(self):
        "等しいかどうかの確認"
        """
        解答が正しいかどうかは、正解と比較して確認します
        To understand reality, we must compare our expectations against reality.
        """
        expected_value = 2
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value)

    def test_a_better_way_of_asserting_equality(self):
        "等しいかどうかのよりよい確認方法"
        """
        assertEqual を使うと、より簡単に確認できます
        Some ways of asserting equality are better than others.
        """
        expected_value = 2
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)

    def test_that_unittest_asserts_work_the_same_way_as_python_asserts(self):
        "Python 組み込みの assert 文"
        """
        unittest モジュール以外に、Python には組み込みの assert 文があります
        Understand what lies within.
        """

        # これは AssertionError 例外を発生させます
        # This throws an AssertionError exception
        assert True

    def test_that_sometimes_we_need_to_know_the_class_type(self):
        "クラスの確認"
        """
        クラス名には何が入っているでしょうか
        What is in a class name?
        """

        # 問題の中には、オブジェクトのクラスが何かを尋ねるものもあります。
        # Sometimes we will ask you what the class type of an object is.
        #
        # 例えば、"navel"という文字列のクラスはなんでしょう。
        # この問題を実行すると、下記のように出力されます。
        # For example, contemplate the text string "navel". What is its class type?
        # The koans runner will include this feedback for this koan:
        #
        #   AssertionError: '-=> FILL ME IN! <=-' != <type 'str'>
        #
        # ということは、"navel".__class__ には <type 'str'> という値が入っているのでしょうか？
        # いいえ。そのように表示されるだけで、入っているのは単に str です。
        # So "navel".__class__ is equal to <type 'str'>? No not quite. This
        # is just what it displays. The answer is simply str.
        #
        # 確かめてみましょう
        # See for yourself:

        self.assertEqual(str, "navel".__class__) # これは str です, <type 'str'> ではありません

        # 画像で確かめたいときはこちら
        # Need an illustration? More reading can be found here:
        #
        #   https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute

