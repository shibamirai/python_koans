#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *

class AboutLists(Koan):
    "リスト"

    def test_creating_lists(self):
        "リストの作成"
        empty_list = list()
        self.assertEqual(list, type(empty_list))
        self.assertEqual(__, len(empty_list))

    def test_list_literals(self):
        "リストの書き方"
        nums = list()
        self.assertEqual([], nums)

        nums[0:] = [1]
        self.assertEqual([1], nums)

        nums[1:] = [2]
        self.assertListEqual([1, __], nums)

        nums.append(333)
        self.assertListEqual([1, 2, __], nums)

    def test_accessing_list_elements(self):
        "要素へのアクセス方法"
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(__, noms[0])
        self.assertEqual(__, noms[3])
        self.assertEqual(__, noms[-1])
        self.assertEqual(__, noms[-3])

    def test_slicing_lists(self):
        "スライス操作"
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(__, noms[0:1])
        self.assertEqual(__, noms[0:2])
        self.assertEqual(__, noms[2:2])
        self.assertEqual(__, noms[2:20])
        self.assertEqual(__, noms[4:0])
        self.assertEqual(__, noms[4:100])
        self.assertEqual(__, noms[5:0])

    def test_slicing_to_the_edge(self):
        "始点、終点を省略したスライス表記"
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(__, noms[2:])
        self.assertEqual(__, noms[:2])

    def test_lists_and_ranges(self):
        "リストと range 関数"
        self.assertEqual(range, type(range(5)))
        self.assertNotEqual([1, 2, 3, 4, 5], range(1,6))
        self.assertEqual(__, list(range(5)))
        self.assertEqual(__, list(range(5, 9)))

    def test_ranges_with_steps(self):
        "step を使った range 関数"
        self.assertEqual(__, list(range(5, 3, -1)))
        self.assertEqual(__, list(range(0, 8, 2)))
        self.assertEqual(__, list(range(1, 8, 3)))
        self.assertEqual(__, list(range(5, -7, -4)))
        self.assertEqual(__, list(range(5, -8, -4)))

    def test_insertions(self):
        "リストへの挿入"
        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
        self.assertEqual(__, knight)

        knight.insert(0, 'Arthur')
        self.assertEqual(__, knight)

    def test_popping_lists(self):
        "pop メソッドの使い方"
        stack = [10, 20, 30, 40]
        stack.append('last')

        self.assertEqual(__, stack)

        popped_value = stack.pop()
        self.assertEqual(__, popped_value)
        self.assertEqual(__, stack)

        popped_value = stack.pop(1)
        self.assertEqual(__, popped_value)
        self.assertEqual(__, stack)

        # "pop" があるのに "push" がないのはなぜでしょう？
        # Notice that there is a "pop" but no "push" in python?

        # Python の哲学には、何かする方法は１つだけであるべきという考え方があるからです
        # 'push' の機能は 'append' と同じです
        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # Python 哲学について知りたいときは、Python コンソールから "import this" と入力してください
        # To learn more about this try typing "import this" from the python
        # console... ;)

    def test_making_queues(self):
        "キュー (先入れ先出しリスト) の作成"
        queue = [1, 2]
        queue.append('last')

        self.assertEqual(__, queue)

        popped_value = queue.pop(0)
        self.assertEqual(__, popped_value)
        self.assertEqual(__, queue)

        # 注意！：実際には、このようにリストの左側からデータを pop させるのは非効率なため、
        # 代わりに collections.deque を使用してください
        # Note, popping from the left hand side of a list is
        # inefficient. Use collections.deque instead.

