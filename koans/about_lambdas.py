#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based slightly on the lambdas section of AboutBlocks in the Ruby Koans
#

from runner.koan import *

class AboutLambdas(Koan):
    "ラムダ式"

    def test_lambdas_can_be_assigned_to_variables_and_called_explicitly(self):
        "ラムダ式は変数に代入して呼び出すことができます"
        add_one = lambda n: n + 1
        self.assertEqual(__, add_one(10))

    # ------------------------------------------------------------------

    def make_order(self, order):
        return lambda qty: str(qty) + " " + order + "s"

    def test_accessing_lambda_via_assignment(self):
        "変数に代入してからのラムダ式の実行"
        sausages = self.make_order('sausage')
        eggs = self.make_order('egg')

        self.assertEqual(__, sausages(3))
        self.assertEqual(__, eggs(2))

    def test_accessing_lambda_without_assignment(self):
        "ラムダ式の直接実行"
        self.assertEqual(__, self.make_order('spam')(39823))
