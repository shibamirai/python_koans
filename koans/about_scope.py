#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

from . import jims
from . import joes

counter = 0 # Global

class AboutScope(Koan):
    "スコープ"
    #
    # NOTE:
    #   ここで使われている Dog クラスの定義は jims.py と joes.py を見てください
    #   Look in jims.py and joes.py to see definitions of Dog used
    #   for this set of tests
    #

    def test_dog_is_not_available_in_the_current_scope(self):
        "このスコープでは Dog クラスは使用できません"
        with self.assertRaises(NameError): fido = Dog()

    def test_you_can_reference_nested_classes_using_the_scope_operator(self):
        "スコープ演算子を使って、入れ子のクラスを参照できます"
        fido = jims.Dog()
        # 'jims' はモジュール名を表し、jims.py のファイル名から取られます
        # name 'jims' module name is taken from jims.py filename

        rover = joes.Dog()
        self.assertEqual('jims dog', fido.identify())
        self.assertEqual('joes dog', rover.identify())

        self.assertEqual(False, type(fido) == type(rover))
        self.assertEqual(False, jims.Dog == joes.Dog)

    # ------------------------------------------------------------------

    class str:
        pass

    def test_bare_bones_class_names_do_not_assume_the_current_scope(self):
        "単純クラス名は現在のスコープのものを表しているわけではありません"
        self.assertEqual(False, AboutScope.str == str)

    def test_nested_string_is_not_the_same_as_the_system_string(self):
        "このスコープの str クラスは、システムの str クラスとは異なります"
        self.assertEqual(False, self.str == type("HI"))

    def test_str_without_self_prefix_stays_in_the_global_scope(self):
        "'self' がついていない str クラスはグローバルスコープのままです"
        self.assertEqual(True, str == type("HI"))

    # ------------------------------------------------------------------

    PI = 3.1416

    def test_constants_are_defined_with_an_initial_uppercase_letter(self):
        "定数は大文字で定義されます"
        self.assertAlmostEqual(3.1416, self.PI)
        # 注意：Python の浮動小数点数は正確ではないので、
        # assertAlmostEqual で'ほぼ等しい'かを調べます
        # Note, floating point numbers in python are not precise.
        # assertAlmostEqual will check that it is 'close enough'

    def test_constants_are_assumed_by_convention_only(self):
        "定数定義は単なる慣例です"
        self.PI = "rhubarb"
        self.assertEqual("rhubarb", self.PI)
        # Python には本当の定数は存在しません。
        # 開発者が慣例で書き換えないようにしているだけです。
        # There aren't any real constants in python. Its up to the developer
        # to keep to the convention and not modify them.

    # ------------------------------------------------------------------

    def increment_using_local_counter(self, counter):
        counter = counter + 1

    def increment_using_global_counter(self):
        global counter
        counter = counter + 1

    def test_incrementing_with_local_counter(self):
        "ローカル変数を使ったインクリメント"
        global counter
        start = counter
        self.increment_using_local_counter(start)
        self.assertEqual(False, counter == start + 1)

    def test_incrementing_with_global_counter(self):
        "グローバル変数を使ったインクリメント"
        global counter
        start = counter
        self.increment_using_global_counter()
        self.assertEqual(True, counter == start + 1)

    # ------------------------------------------------------------------

    def local_access(self):
        stuff = 'eels'
        def from_the_league():
            stuff = 'this is a local shop for local people'
            return stuff
        return from_the_league()

    def nonlocal_access(self):
        stuff = 'eels'
        def from_the_boosh():
            nonlocal stuff
            return stuff
        return from_the_boosh()

    def test_getting_something_locally(self):
        "ローカル変数の取得"
        self.assertEqual('this is a local shop for local people', self.local_access())

    def test_getting_something_nonlocally(self):
        "ノンローカル変数の取得"
        self.assertEqual('eels', self.nonlocal_access())

    # ------------------------------------------------------------------

    global deadly_bingo
    deadly_bingo = [4, 8, 15, 16, 23, 42]

    def test_global_attributes_can_be_created_in_the_middle_of_a_class(self):
        "グローバル属性はクラスの途中で作ることもできます"
        self.assertEqual(42, deadly_bingo[5])
