#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

def function():
    return "pineapple"

def function2():
    return "tractor"

class Class:
    def method(self):
        return "parrot"

class AboutMethodBindings(Koan):
    "メソッドの束縛（バインディング）"

    def test_methods_are_bound_to_an_object(self):
        "メソッドはオブジェクトに束縛(bound)されています"
        obj = Class()
        self.assertEqual(True, obj.method.__self__ == obj)

    def test_methods_are_also_bound_to_a_function(self):
        "メソッドは関数オブジェクトにも束縛されています"
        obj = Class()
        self.assertEqual("parrot", obj.method())
        self.assertEqual("parrot", obj.method.__func__(obj))

    def test_functions_have_attributes(self):
        "関数は属性を持ちます"
        obj = Class()
        self.assertEqual(35, len(dir(function)))
        self.assertEqual(True, dir(function) == dir(obj.method.__func__))

    def test_methods_have_different_attributes(self):
        "メソッドは関数とは異なる属性を持ちます"
        obj = Class()
        self.assertEqual(27, len(dir(obj.method)))

    def test_setting_attributes_on_an_unbound_function(self):
        "関数への属性の追加"
        function.cherries = 3
        self.assertEqual(3, function.cherries)

    def test_setting_attributes_on_a_bound_method_directly(self):
        "メソッドへ直接属性を追加する"
        obj = Class()
        with self.assertRaises(AttributeError): obj.method.cherries = 3

    def test_setting_attributes_on_methods_by_accessing_the_inner_function(self):
        "関数オブジェクトを通じてメソッドに属性を追加する"
        obj = Class()
        obj.method.__func__.cherries = 3
        self.assertEqual(3, obj.method.cherries)

    def test_functions_can_have_inner_functions(self):
        "関数は内部関数を持つことができます"
        function2.get_fruit = function
        self.assertEqual("pineapple", function2.get_fruit())

    def test_inner_functions_are_unbound(self):
        "内部関数はオブジェクトに束縛されません"
        function2.get_fruit = function
        with self.assertRaises(AttributeError): cls = function2.get_fruit.__self__

    # ------------------------------------------------------------------

    class BoundClass:
        def __get__(self, obj, cls):
            return (self, obj, cls)

    binding = BoundClass()

    def test_get_descriptor_resolves_attribute_binding(self):
        "get デスクリプタは属性の束縛先を決めます"
        bound_obj, binding_owner, owner_type = self.binding
        # BoundClass の __get__() を参照：
        # Look at BoundClass.__get__():
        #   bound_obj = self
        #   binding_owner = obj
        #   owner_type = cls

        self.assertEqual("BoundClass", bound_obj.__class__.__name__)
        self.assertEqual("AboutMethodBindings", binding_owner.__class__.__name__)
        self.assertEqual(AboutMethodBindings, owner_type)

    # ------------------------------------------------------------------

    class SuperColor:
        def __init__(self):
            self.choice = None

        def __set__(self, obj, val):
            self.choice = val

    color = SuperColor()

    def test_set_descriptor_changes_behavior_of_attribute_assignment(self):
        "set デスクリプタは属性への代入の挙動を変更します"
        self.assertEqual(None, self.color.choice)
        self.color = 'purple'
        self.assertEqual('purple', self.color.choice)

