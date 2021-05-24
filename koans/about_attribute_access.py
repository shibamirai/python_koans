#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Partially based on AboutMessagePassing in the Ruby Koans
#

from runner.koan import *

class AboutAttributeAccess(Koan):
    "属性へのアクセス"

    class TypicalObject:
        pass

    def test_calling_undefined_functions_normally_results_in_errors(self):
        "未定義の関数を呼ぶとエラーになります"
        typical = self.TypicalObject()

        with self.assertRaises(AttributeError): typical.foobar()

    def test_calling_getattribute_causes_an_attribute_error(self):
        "(未定義の属性に対して)__getattribute__ を呼ぶと AttributeError が発生します"
        typical = self.TypicalObject()

        with self.assertRaises(AttributeError): typical.__getattribute__('foobar')

        # 考えてみましょう：
        # THINK ABOUT IT:
        #
        # もし __getattribute__() メソッドが AttributeError を起こすのであれば、
        # __getattribute__() をオーバーライドするとなにが起こるのでしょうか？
        # If the method __getattribute__() causes the AttributeError, then
        # what would happen if we redefine __getattribute__()?

    # ------------------------------------------------------------------

    class CatchAllAttributeReads:
        def __getattribute__(self, attr_name):
            return "Someone called '" + attr_name + "' and it could not be found"

    def test_all_attribute_reads_are_caught(self):
        "__getattribute__ は、すべての属性参照で呼び出されます"
        catcher = self.CatchAllAttributeReads()

        self.assertRegex(catcher.foobar, 'Someone called')

    def test_intercepting_return_values_can_disrupt_the_call_chain(self):
        "戻り値に割り込むと、呼び出しチェーンが混乱します"
        catcher = self.CatchAllAttributeReads()

        self.assertRegex(catcher.foobaz, 'Someone called') # これは問題なし This is fine

        try:
            catcher.foobaz(1)
        except TypeError as ex:
            err_msg = ex.args[0]

        self.assertRegex(err_msg, "'str' object is not callable")

        # foobaz は(__getattribute__()が返す)文字列を返します。ではその後の
        # '(1)' では何が起こるのでしょうか？
        # python コンソールで下記を入力して、再現してみましょう：
        # foobaz returns a string. What happens to the '(1)' part?
        # Try entering this into a python console to reproduce the issue:
        #
        #     "foobaz"(1)
        #

    def test_changes_to_the_getattribute_implementation_affects_getattr_function(self):
        "__getattribuite__ の変更は、__getattr__ にも影響します"
        catcher = self.CatchAllAttributeReads()

        self.assertRegex(getattr(catcher, 'any_attribute'), 'Someone called')

    # ------------------------------------------------------------------

    class WellBehavedFooCatcher:
        def __getattribute__(self, attr_name):
            if attr_name[:3] == "foo":
                return "Foo to you too"
            else:
                return super().__getattribute__(attr_name)

    def test_foo_attributes_are_caught(self):
        "'foo'から始まる属性をキャッチします"
        catcher = self.WellBehavedFooCatcher()

        self.assertEqual("Foo to you too", catcher.foo_bar)
        self.assertEqual("Foo to you too", catcher.foo_baz)

    def test_non_foo_messages_are_treated_normally(self):
        "'foo'以外の属性は通常通りの扱いです"
        catcher = self.WellBehavedFooCatcher()

        with self.assertRaises(AttributeError): catcher.normal_undefined_attribute

    # ------------------------------------------------------------------

    global stack_depth
    stack_depth = 0

    class RecursiveCatcher:
        def __init__(self):
            global stack_depth
            stack_depth = 0
            self.no_of_getattribute_calls = 0

        def __getattribute__(self, attr_name):
            # このクラスのスコープ外の変数が必要です
            # We need something that is outside the scope of this class:
            global stack_depth
            stack_depth += 1

            if stack_depth<=10: # スタックオーバーフロー対策 to prevent a stack overflow
                self.no_of_getattribute_calls += 1
                # あっ！属性 (no_of_getattribute_calls) にアクセスしてしまいました
                # 何が起こるでしょうか？
                # Oops! We just accessed an attribute (no_of_getattribute_calls)
                # Guess what happens when self.no_of_getattribute_calls is
                # accessed?

            # ここで super() を使うと、それに対する __getattribute__() 呼び出しが
            # 発生してしまうので、直接 'object' を使います
            # Using 'object' directly because using super() here will also
            # trigger a __getattribute__() call.
            return object.__getattribute__(self, attr_name)

        def my_method(self):
            pass

    def test_getattribute_is_a_bit_overzealous_sometimes(self):
        "時々 __getattribute__ は張り切りすぎます"
        catcher = self.RecursiveCatcher()
        catcher.my_method()
        global stack_depth
        self.assertEqual(11, stack_depth)

    # ------------------------------------------------------------------

    class MinimalCatcher:
        class DuffObject: pass

        def __init__(self):
            self.no_of_getattr_calls = 0

        def __getattr__(self, attr_name):
            self.no_of_getattr_calls += 1
            return self.DuffObject

        def my_method(self):
            pass

    def test_getattr_ignores_known_attributes(self):
        "__getattr__ は定義済み属性を無視します"
        catcher = self.MinimalCatcher()
        catcher.my_method()

        self.assertEqual(0, catcher.no_of_getattr_calls)

    def test_getattr_only_catches_unknown_attributes(self):
        "__getattr__ は未定義の属性だけをキャッチします"
        catcher = self.MinimalCatcher()
        catcher.purple_flamingos()
        catcher.free_pie()

        self.assertEqual("DuffObject",
            type(catcher.give_me_duff_or_give_me_death()).__name__)

        self.assertEqual(3, catcher.no_of_getattr_calls)

    # ------------------------------------------------------------------

    class PossessiveSetter(object):
        def __setattr__(self, attr_name, value):
            new_attr_name =  attr_name

            if attr_name[-5:] == 'comic':
                new_attr_name = "my_" + new_attr_name
            elif attr_name[-3:] == 'pie':
                new_attr_name = "a_" + new_attr_name

            object.__setattr__(self, new_attr_name, value)

    def test_setattr_intercepts_attribute_assignments(self):
        "__setattr__ は属性の割り当て時に割り込みます"
        fanboy = self.PossessiveSetter()

        fanboy.comic = 'The Laminator, issue #1'
        fanboy.pie = 'blueberry'

        self.assertEqual('blueberry', fanboy.a_pie)

        #
        # 注意：次の assert に合格するよう、prefix の値を変更してください
        # NOTE: Change the prefix to make this next assert pass
        #

        prefix = 'my'
        self.assertEqual("The Laminator, issue #1", getattr(fanboy, prefix + '_comic'))

    # ------------------------------------------------------------------

    class ScarySetter:
        def __init__(self):
            self.num_of_coconuts = 9
            self._num_of_private_coconuts = 2

        def __setattr__(self, attr_name, value):
            new_attr_name =  attr_name

            if attr_name[0] != '_':
                new_attr_name = "altered_" + new_attr_name

            object.__setattr__(self, new_attr_name, value)

    def test_it_modifies_external_attribute_as_expected(self):
        "__setattr__ は、未定義の属性を思ったように書き換えます"
        setter = self.ScarySetter()
        setter.e = "mc hammer"

        self.assertEqual("mc hammer", setter.altered_e)

    def test_it_mangles_some_internal_attributes(self):
        "__setattr__ は、時々定義済みの属性を台無しにします"
        setter = self.ScarySetter()

        try:
            coconuts = setter.num_of_coconuts
        except AttributeError:
            self.assertEqual(9, setter.altered_num_of_coconuts)

    def test_in_this_case_private_attributes_remain_unmangled(self):
        "このケースでは、プライベート属性はそのままです"
        setter = self.ScarySetter()

        self.assertEqual(2, setter._num_of_private_coconuts)
