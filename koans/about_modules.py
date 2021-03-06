#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This is very different to AboutModules in Ruby Koans
# Our AboutMultipleInheritance class is a little more comparable
#

from runner.koan import *

from .another_local_module import *
from .local_module_with_all_defined import *


class AboutModules(Koan):
    "モジュール"
    def test_importing_other_python_scripts_as_modules(self):
        "他の python スクリプトをモジュールとしてインポート"
        from . import local_module  # local_module.py

        duck = local_module.Duck()
        self.assertEqual(__, duck.name)

    def test_importing_attributes_from_classes_using_from_keyword(self):
        "from 句を使ってクラスから属性をインポート"
        from .local_module import Duck

        duck = Duck()  # 今度はモジュール識別子は不要 no module qualifier needed this time
        self.assertEqual(__, duck.name)

    def test_we_can_import_multiple_items_at_once(self):
        "一度に複数の項目をインポートできます"
        from . import jims, joes

        jims_dog = jims.Dog()
        joes_dog = joes.Dog()
        self.assertEqual(__, jims_dog.identify())
        self.assertEqual(__, joes_dog.identify())

    def test_importing_all_module_attributes_at_once(self):
        "一度にすべてのモジュール属性をインポートする"
        """
        すべてをインポートするには以下のように記述します：
        importing all attributes at once is done like so:
            from .another_local_module import *
        ワイルドカードはクラスや関数の中では使えません
        The import wildcard cannot be used from within classes or functions.
        """

        goose = Goose()
        hamster = Hamster()

        self.assertEqual(__, goose.name)
        self.assertEqual(__, hamster.name)

    def test_modules_hide_attributes_prefixed_by_underscores(self):
        "モジュールはアンダースコアから始まる属性を隠します"
        with self.assertRaises(___):
            private_squirrel = _SecretSquirrel()

    def test_private_attributes_are_still_accessible_in_modules(self):
        "プライベート属性はまだアクセス可能です"
        from .local_module import Duck  # local_module.py

        duck = Duck()
        self.assertEqual(__, duck._password)
        # モジュール階層での隠匿はクラス属性には影響しません
        # (クラス自身が隠されていなければですが)
        # module level attribute hiding doesn't affect class attributes
        # (unless the class itself is hidden).

    def test_a_module_can_limit_wildcard_imports(self):
        "モジュールはワイルドカードでのインポートを制限できます"
        """
        次の例を見てみましょう：
        Examine results of:
            from .local_module_with_all_defined import *
        """

        # 'Goat' は __all__ リストに載っています
        # 'Goat' is on the __all__ list
        goat = Goat()
        self.assertEqual(__, goat.name)

        # velociraptors はどうでしょう？
        # How about velociraptors?
        lizard = _Velociraptor()
        self.assertEqual(__, lizard.name)

        # SecretDuck? 聞いたことないですね！
        # SecretDuck? Never heard of her!
        with self.assertRaises(___):
            duck = SecretDuck()
