#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutInheritance(Koan):
    "クラスの継承"

    class Dog:
        def __init__(self, name):
            self._name = name

        @property
        def name(self):
            return self._name

        def bark(self):
            return "WOOF"

    class Chihuahua(Dog):
        def wag(self):
            return "happy"

        def bark(self):
            return "yip"

    def test_subclasses_have_the_parent_as_an_ancestor(self):
        "サブクラスは親を持ちます"
        self.assertEqual(__, issubclass(self.Chihuahua, self.Dog))

    def test_all_classes_in_python_3_ultimately_inherit_from_object_class(self):
        "Python 3 のすべてのクラスは object クラスを継承します"
        self.assertEqual(__, issubclass(self.Chihuahua, object))

        # 注意：Python 2 では異なり、組み込みクラスか object クラスを明示的に
        # 継承しなければなりません
        # Note: This isn't the case in Python 2. In that version you have
        # to inherit from a built in class or object explicitly

    def test_instances_inherit_behavior_from_parent_class(self):
        "インスタンスは親クラスの振る舞いを継承します"
        chico = self.Chihuahua("Chico")
        self.assertEqual(__, chico.name)

    def test_subclasses_add_new_behavior(self):
        "サブクラスには新しい振る舞いを追加できます"
        chico = self.Chihuahua("Chico")
        self.assertEqual(__, chico.wag())

        fido = self.Dog("Fido")
        with self.assertRaises(___): fido.wag()

    def test_subclasses_can_modify_existing_behavior(self):
        "サブクラスでは親クラスの振る舞いを書き換えることができます"
        chico = self.Chihuahua("Chico")
        self.assertEqual(__, chico.bark())

        fido = self.Dog("Fido")
        self.assertEqual(__, fido.bark())

    # ------------------------------------------------------------------

    class BullDog(Dog):
        def bark(self):
            return super().bark() + ", GRR"
            # super() は Python 3 で書き方が簡単になりました！
            # Note, super() is much simpler to use in Python 3!

    def test_subclasses_can_invoke_parent_behavior_via_super(self):
        "super を使って、サブクラスから親クラスの振る舞いを呼び出せます"
        ralph = self.BullDog("Ralph")
        self.assertEqual(__, ralph.bark())

    # ------------------------------------------------------------------

    class GreatDane(Dog):
        def growl(self):
            return super().bark() + ", GROWL"

    def test_super_works_across_methods(self):
        "super はメソッドを通じて機能します"
        george = self.GreatDane("George")
        self.assertEqual(__, george.growl())

    # ---------------------------------------------------------

    class Pug(Dog):
        def __init__(self, name):
            pass

    class Greyhound(Dog):
        def __init__(self, name):
            super().__init__(name)

    def test_base_init_does_not_get_called_automatically(self):
        "親クラスの init は、自動的に呼ばれる訳ではありません"
        snoopy = self.Pug("Snoopy")
        with self.assertRaises(___): name = snoopy.name

    def test_base_init_has_to_be_called_explicitly(self):
        "親クラスの init は明示的に呼び出す必要があります"
        boxer = self.Greyhound("Boxer")
        self.assertEqual(__, boxer.name)
