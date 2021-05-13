#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# この問題は、triangle.py の triangle 関数を修正してください
# You need to finish implementing triangle() in the file 'triangle.py'
from .triangle import *

class AboutTriangleProject2(Koan):
    "三角形プロジェクト パート2"
    # パート1ではエラーを扱っていなかったので、ここで扱えるようにしましょう
    # The first assignment did not talk about how to handle errors.
    # Let's handle that part now.
    def test_illegal_triangles_throw_exceptions(self):
        "不正な三角形では例外が発生します"
        # 3辺はすべて 0 より大きくなければなりません
        # All sides should be greater than 0
        with self.assertRaises(TriangleError):
            triangle(0, 0, 0)
        with self.assertRaises(TriangleError):
            triangle(3, 4, -5)

        # 2辺の和は残り1辺より大きくなければなりません
        # The sum of any two sides should be greater than the third one
        with self.assertRaises(TriangleError):
            triangle(1, 1, 3)
        with self.assertRaises(TriangleError):
            triangle(2, 5, 2)


