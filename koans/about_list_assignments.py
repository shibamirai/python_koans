#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrayAssignments in the Ruby Koans
#

from runner.koan import *

class AboutListAssignments(Koan):
    "リストの割り当て"

    def test_non_parallel_assignment(self):
        "アンパック代入ではない通常の代入"
        names = ["John", "Smith"]
        self.assertEqual(["John", "Smith"], names)

    def test_parallel_assignments(self):
        "アンパック代入"
        first_name, last_name = ["John", "Smith"]
        self.assertEqual("John", first_name)
        self.assertEqual("Smith", last_name)

    def test_parallel_assignments_with_extra_values(self):
        "アスタリスクを使ったアンパック"
        title, *first_names, last_name = ["Sir", "Ricky", "Bobby", "Worthington"]
        self.assertEqual("Sir", title)
        self.assertEqual(["Ricky", "Bobby"], first_names)
        self.assertEqual("Worthington", last_name)

    def test_parallel_assignments_with_sublists(self):
        "入れ子のリストのアンパック"
        first_name, last_name = [["Willie", "Rae"], "Johnson"]
        self.assertEqual(["Willie", "Rae"], first_name)
        self.assertEqual("Johnson", last_name)

    def test_swapping_with_parallel_assignment(self):
        "複数代入による値の入れ替え"
        first_name = "Roy"
        last_name = "Rob"
        first_name, last_name = last_name, first_name
        self.assertEqual("Rob", first_name)
        self.assertEqual("Roy", last_name)

