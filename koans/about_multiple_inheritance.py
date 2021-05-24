#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Slightly based on AboutModules in the Ruby Koans
#

from runner.koan import *

class AboutMultipleInheritance(Koan):
    "多重継承"

    class Nameable:
        def __init__(self):
            self._name = None

        def set_name(self, new_name):
            self._name = new_name

        def here(self):
            return "In Nameable class"

    class Animal:
        def legs(self):
            return 4

        def can_climb_walls(self):
            return False

        def here(self):
            return "In Animal class"

    class Pig(Animal):
        def __init__(self):
            super().__init__()
            self._name = "Jasper"

        @property
        def name(self):
            return self._name

        def speak(self):
            return "OINK"

        def color(self):
            return 'pink'

        def here(self):
            return "In Pig class"

    class Spider(Animal):
        def __init__(self):
            super().__init__()
            self._name = "Boris"

        def can_climb_walls(self):
            return True

        def legs(self):
            return 8

        def color(self):
            return 'black'

        def here(self):
            return "In Spider class"

    class Spiderpig(Pig, Spider, Nameable):
        def __init__(self):
            super(AboutMultipleInheritance.Pig, self).__init__()
            super(AboutMultipleInheritance.Nameable, self).__init__()
            self._name = "Jeff"

        def speak(self):
            return "This looks like a job for Spiderpig!"

        def here(self):
            return "In Spiderpig class"

    #
    # クラス階層 Hierarchy:
    #               Animal
    #              /     \
    #            Pig   Spider  Nameable
    #              \      |      /
    #                 Spiderpig
    #
    # ------------------------------------------------------------------

    def test_normal_methods_are_available_in_the_object(self):
        "通常のメソッドはそのオブジェクトで使用できます"
        jeff = self.Spiderpig()
        self.assertRegex(jeff.speak(), "This looks like a job for Spiderpig!")

    def test_base_class_methods_are_also_available_in_the_object(self):
        "親クラスのメソッドも使用できます"
        jeff = self.Spiderpig()
        try:
            jeff.set_name("Rover")
        except:
            self.fail("This should not happen")
        self.assertEqual(True, jeff.can_climb_walls())

    def test_base_class_methods_can_affect_instance_variables_in_the_object(self):
        "親クラスのメソッドは、そのオブジェクトのインスタンス変数にも影響を与えます"
        jeff = self.Spiderpig()
        self.assertEqual("Jeff", jeff.name)

        jeff.set_name("Rover")
        self.assertEqual("Rover", jeff.name)

    def test_left_hand_side_inheritance_tends_to_be_higher_priority(self):
        "継承順が左側の方が、より優先度が高くなります"
        jeff = self.Spiderpig()
        self.assertEqual('pink', jeff.color())

    def test_super_class_methods_are_higher_priority_than_super_super_classes(self):
        "親クラスのメソッドの方が、親の親のものより優先度が高くなります"
        jeff = self.Spiderpig()
        self.assertEqual(8, jeff.legs())

    def test_we_can_inspect_the_method_resolution_order(self):
        "メソッドの解決順を見てみましょう"
        #
        # MRO = メソッド解決順 Method Resolution Order
        #
        mro = type(self.Spiderpig()).mro()
        self.assertEqual('Spiderpig', mro[0].__name__)
        self.assertEqual('Pig', mro[1].__name__)
        self.assertEqual('Spider', mro[2].__name__)
        self.assertEqual('Animal', mro[3].__name__)
        self.assertEqual('Nameable', mro[4].__name__)
        self.assertEqual('object', mro[5].__name__)

    def test_confirm_the_mro_controls_the_calling_order(self):
        "MRO が呼び出し順序を制御していることを確認します"
        jeff = self.Spiderpig()
        self.assertRegex(jeff.here(), 'Spiderpig')

        next = super(AboutMultipleInheritance.Spiderpig, jeff)
        self.assertRegex(next.here(), 'Pig')

        next = super(AboutMultipleInheritance.Pig, jeff)
        self.assertRegex(next.here(), 'Spider')

        # ちょっと待ってください!? 最後のクラス名は 'jeff' の親クラスではありますが
        # Pig の親クラスではありませんよね？
        # Hang on a minute?!? That last class name might be a super class of
        # the 'jeff' object, but its hardly a superclass of Pig, is it?
        #
        # 混乱しないようにするには、super() は next_mro() だと考えるといいでしょう。
        # To avoid confusion it may help to think of super() as next_mro().
