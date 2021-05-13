#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutNil in the Ruby Koans
#

from runner.koan import *

class AboutNone(Koan):
    "None とは"

    def test_none_is_an_object(self):
        "None はオブジェクトです"
        "多くの言語で使われる NULL とは違います"
        "Unlike NULL in a lot of languages"
        self.assertEqual(__, isinstance(None, object))

    def test_none_is_universal(self):
        "None は１つしかありません"
        "There is only one None"
        self.assertEqual(____, None is None)

    def test_what_exception_do_you_get_when_calling_nonexistent_methods(self):
        "存在しないメソッドを呼び出すと発生する例外は？"
        """
        存在しないメソッドを呼び出したときに発生する例外はなんでしょう？
        What is the Exception that is thrown when you call a method that does
        not exist?

        ヒント：Python コンソールで下記コードを実行してみましょう
        Hint: launch python command console and try the code in the block below.

        'try' や 'except' が何かは、今は分からなくても大丈夫です
        Don't worry about what 'try' and 'except' do, we'll talk about this later
        """
        try:
            None.some_method_none_does_not_know_about()
        except Exception as ex:
            ex2 = ex

        # どんな例外が発生しましたか？
        # What exception has been caught?
        #
        # __class__ にはどのような値が入っているんでしたでしょうか？
        # Need a recap on how to evaluate __class__ attributes?
        #
        #     https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute

        self.assertEqual(__, ex2.__class__)

        # 例外メッセージには何が入っていましたか？
        # (ヒント：__ をエラーメッセージの一部と置き換えてください)
        # What message was attached to the exception?
        # (HINT: replace __ with part of the error message.)
        self.assertRegex(ex2.args[0], __)

    def test_none_is_distinct(self):
        "None は False 等、他の値とは異なります"
        """
        None is distinct from other things which are False.
        """
        self.assertEqual(__, None is not 0)
        self.assertEqual(__, None is not False)
