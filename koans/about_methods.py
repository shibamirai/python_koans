#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Partially based on AboutMethods in the Ruby Koans
#

from runner.koan import *

def my_global_function(a,b):
    return a + b

class AboutMethods(Koan):
    "メソッド"

    def test_calling_a_global_function(self):
        "グローバル関数の呼び出し"
        self.assertEqual(__, my_global_function(2,3))

    # 注意：引数の個数の誤りはシンタックスエラーではなく実行時エラーになります
    # NOTE: Wrong number of arguments is not a SYNTAX error, but a
    # runtime error.
    def test_calling_functions_with_wrong_number_of_arguments(self):
        "引数の個数を間違って呼び出すと？"
        try:
            my_global_function()
        except TypeError as exception:
            msg = exception.args[0]

        # 注意：下記の文字列比較は Python 3.2 ではまだうまくいきますが、
        # 過去に変更されたこともあるため、将来うまくいかなくなるかもしれません。
        # Note, the text comparison works for Python 3.2
        # It has changed in the past and may change in the future
        self.assertRegex(msg,
            r'my_global_function\(\) missing 2 required positional arguments')

        try:
            my_global_function(1, 2, 3)
        except Exception as e:
            msg = e.args[0]

        # 注意：丸カッコ '(' ')' の前にはバックスラッシュが必要です！
        # Note, watch out for parenthesis. They need slashes in front!
        self.assertRegex(msg, __)

    # ------------------------------------------------------------------

    def pointless_method(self, a, b):
        sum = a + b

    def test_which_does_not_return_anything(self):
        "値を返さないメソッドの戻り値は？"
        self.assertEqual(__, self.pointless_method(1, 2))
        # クラス内のメソッドの第一引数 "self" は、呼び出し時に指定する必要がないことに
        # 気づきましたか？
        # Notice that methods accessed from class scope do not require
        # you to pass the first "self" argument?

    # ------------------------------------------------------------------

    def method_with_defaults(self, a, b='default_value'):
        return [a, b]

    def test_calling_with_default_values(self):
        "デフォルト引数"
        self.assertEqual(__, self.method_with_defaults(1))
        self.assertEqual(__, self.method_with_defaults(1, 2))

    # ------------------------------------------------------------------

    def method_with_var_args(self, *args):
        return args

    def test_calling_with_variable_arguments(self):
        "可変長引数"
        self.assertEqual(__, self.method_with_var_args())
        self.assertEqual(('one',), self.method_with_var_args('one'))
        self.assertEqual(__, self.method_with_var_args('one', 'two'))

    # ------------------------------------------------------------------

    def function_with_the_same_name(self, a, b):
        return a + b

    def test_functions_without_self_arg_are_global_functions(self):
        "self 引数がないメソッドはグローバル関数になります"
        def function_with_the_same_name(a, b):
            return a * b

        self.assertEqual(__, function_with_the_same_name(3,4))

    def test_calling_methods_in_same_class_with_explicit_receiver(self):
        "明示的にレシーバ（オブジェクト）を指定してのメソッド呼び出し"
        def function_with_the_same_name(a, b):
            return a * b

        self.assertEqual(__, self.function_with_the_same_name(3,4))

    # ------------------------------------------------------------------

    def another_method_with_the_same_name(self):
        return 10

    link_to_overlapped_method = another_method_with_the_same_name

    def another_method_with_the_same_name(self):
        return 42

    def test_that_old_methods_are_hidden_by_redefinitions(self):
        "メソッドを再定義すると古い定義は見えなくなります"
        self.assertEqual(__, self.another_method_with_the_same_name())

    def test_that_overlapped_method_is_still_there(self):
        "でもなくなったわけではありません"
        self.assertEqual(__, self.link_to_overlapped_method())

    # ------------------------------------------------------------------

    def empty_method(self):
        pass

    def test_methods_that_do_nothing_need_to_use_pass_as_a_filler(self):
        "空のメソッドには pass 文を書く必要があります"
        self.assertEqual(__, self.empty_method())

    def test_pass_does_nothing_at_all(self):
        "pass 文は何もせず素通りします"
        "You"
        "shall"
        "not"
        pass
        self.assertEqual(____, "Still got to this line" != None)

    # ------------------------------------------------------------------

    def one_line_method(self): return 'Madagascar'

    def test_no_indentation_required_for_one_line_statement_bodies(self):
        "メソッドを1行で定義するときは、インデントは不要です"
        self.assertEqual(__, self.one_line_method())

    # ------------------------------------------------------------------

    def method_with_documentation(self):
        "A string placed at the beginning of a function is used for documentation"
        return "ok"

    def test_the_documentation_can_be_viewed_with_the_doc_method(self):
        "ドキュメンテーション文字列は __doc__ で参照できます"
        self.assertRegex(self.method_with_documentation.__doc__, __)

    # ------------------------------------------------------------------

    class Dog:
        def name(self):
            return "Fido"

        def _tail(self):
            # アンダースコア１つから始まる名前は private スコープであることを示します
            # Prefixing a method with an underscore implies private scope
            return "wagging"

        def __password(self):
            return 'password' # Genius!

    def test_calling_methods_in_other_objects(self):
        "別オブジェクトからのメソッドの呼び出し"
        rover = self.Dog()
        self.assertEqual(__, rover.name())

    def test_private_access_is_implied_but_not_enforced(self):
        "private アクセスは強制されるわけではありません"
        rover = self.Dog()

        # 不作法ですが、違反ではありません
        # This is a little rude, but legal
        self.assertEqual(__, rover._tail())

    def test_attributes_with_double_underscore_prefixes_are_subject_to_name_mangling(self):
        "アンダースコア２つから始まる名前にはネームマングリング機構が働きます"
        rover = self.Dog()
        with self.assertRaises(___): password = rover.__password()

        # でもこうするとアクセスできてしまいます!
        # But this still is!
        self.assertEqual(__, rover._Dog__password())

        # ネームマングリング機構は親クラスと子クラス間での名前衝突を避けるために存在します。
        # アクセス制御のためではありません。
        # Name mangling exists to avoid name clash issues when subclassing.
        # It is not for providing effective access protection
